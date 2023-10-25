---
meta:
    id: cboe
  # ks-debug: true
    encoding: ASCII
    endian: le
seq:
  - id: records
    type: record(_index, _io.pos)
    # size-eos: true
    eos-error: false
    repeat: eos
instances:
    num_record_entries:
        value: records.size
    record_type_mask:
        value: 0x08
        doc: Magic number to offset the position of the msgtype char in record.
types:
    record:
        params:
          - id: idx
            type: u4
          - id: ofs
            type: u4
        seq:
          - id: start_of_line
            contents: S
            doc: Magic starting char "S"
          - id: raw
            type: strz
            terminator: 0xd
            consume: false
            include: false
          - id: end_of_line
            contents: [0xd, 0xa] # CRLF
        instances:
            type_indicator:
                io: _root._io
                pos: data_offset + _root.record_type_mask
                size: 1
                type: str
            data:
                io: _root._io
                pos: data_offset
                size: data_size
                type:
                    switch-on: type_indicator
                    cases:
                        '"B"': trade_break_message
                        '"X"': order_cancel_message
                        '"J"': auction_summary_message
                        '"H"': trading_status_message
                        '"s"': symbol_clear_message
                        '"A"': add_order_message_short
                        '"I"': auction_update_message
                        '"P"': trade_message_short
                        '"R"': retail_price_improvement_message
                        '"r"': trade_message_long
                        '"E"': order_executed_message
                        '"d"': add_order_message_long
            data_offset:
                value: ofs + 1
            data_size:
                value: raw.length
    block:
        params:
          - id: type
            type: str
          - id: offset
            type: u2
          - id: length
            type: u2
        seq:
          - id: value
            size: length
            type: strz
    trade_break_message:
        doc: >-
            The Trade Break message is sent whenever an execution on Cboe is broken.
            Trade breaks are rare and only affect applications that rely upon Cboe
            execution based data. Applications that simply build a Cboe book can
            ignore Trade Break messages.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Trade Break message
            type: block('alpha', 8, 1)
          - id: execution_id
            doc: >-
                Cboe execution identifier of the execution that was broken.
                Execution ID refers to previously sent Order Execution or Trade
                message.
            type: block('base_36_numeric', 9, 12)
    order_cancel_message:
        doc: >-
            Order Cancel messages are sent when a visible order on the Cboe book is
            canceled in whole or in part.

            NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously
            sent with an Add Order message. Multiple Order Modification messages may
            modify a single order and the effects are cumulative. Order Modification
            messages always reduce the remaining shares in the referenced open order
            by the number of shares indicated. When the remaining shares for an order
            reach zero, the order is dead and should be removed from the book.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Order Cancel message
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Order ID of a previously sent Add Order Message that has been reduced or cancelled
            type: block('base_36_numeric', 9, 12)
          - id: canceled_shares
            doc: Number of shares canceled
            type: block('numeric', 21, 6)
    auction_summary_message:
        doc: >-
            Auction Summary messages are used to disseminate the results of an auction
            of a Cboe listed security. An Opening Auction Summary message for each
            Cboe listed security is sent at the conclusion of its opening auction at
            9:30 a.m. and represents the Cboe official opening price. A Closing
            Auction Summary message for each Cboe listed security is sent at the
            conclusion of its closing auction at 4:00 p.m. and represents the Cboe
            official closing price. An IPO Auction Summary message for each Cboe
            listed security is sent at the conclusion of the IPO Auction and
            represents the official Cboe IPO opening price.

            Cboe Auction Summary messages support the Cboe Opening, Closing, Halt and
            IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction
            Process specification for more information on Cboe Auctions.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Auction Summary message
            type: block('alpha', 8, 1)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 9, 8)
          - id: auction_type
            doc: |-
                O = Opening Auction
                C = Closing Auction
                H = Halt Auction
                I = IPO Auction
            type: block('alpha', 17, 1)
          - id: price
            doc: Auction price
            type: block('price', 18, 10)
          - id: shares
            doc: Cumulative number of shares  executed during the auction
            type: block('numeric', 28, 10)
    trading_status_message:
        doc: >-
            The Trading Status message is used to indicate the current trading status
            of a security. A Trading Status message will be sent whenever a security’s
            trading status changes. In addition, Cboe will send a Trading Status
            message for all securities that are “Halted” or have a price test in
            effect before the start of trading hours.

            Trading Status of `S` will be implied at system startup. `T` will be sent
            as securities are available for trading. `A` will be distributed when
            orders can be accepted for queuing in preparation for the market open.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Trading Status message
            type: block('alpha', 8, 1)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 9, 8)
          - id: halt_status
            doc: |-
                A = Accepting Orders for Queuing
                H = Halted
                Q = Quote-Only (Cboe Listings)
                S = Exchange Specific Suspension
                T = Trading
            type: block('alpha', 17, 1)
          - id: reg_sho_action
            doc: |-
                0 = No price test in effect
                1 = Reg SHO price test restriction in effect
            type: block('numeric', 18, 1)
          - id: reserved1
            doc: Reserved
            type: block('alpha', 19, 1)
          - id: reserved2
            doc: Reserved
            type: block('alpha', 20, 1)
    symbol_clear_message:
        doc: >-
            The Symbol Clear message instructs feed recipients to clear all orders for
            the Cboe book in the specified symbol. This message will be sent at
            startup each day. It would also be distributed in certain recovery events
            such as a data center fail-over.
        seq:
          - id: timestamp
            doc: TimeStamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Symbol Clear Message
            type: block('alpha', 8, 1)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 9, 8)
    add_order_message_short:
        doc: >-
            An Add Order message represents a newly accepted visible order on the Cboe
            book. It includes a day-specific Order ID assigned by Cboe to the order.
            The Display field is used to reflect whether or not the order can be
            considered a protected quote and thus reportable to the SIP.

            NOTE: If an order’s Price or Display values change within the Cboe
            matching engine, a Cancel Order Message will be immediately followed by a
            new Add Order message with the same Order ID as the original order. An
            order that changes its Display value from “N” to “Y” will not lose its
            priority.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Add Order message (short)
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Day-specific identifier assigned to this order
            type: block('base_36_numeric', 9, 12)
          - id: side_indicator
            doc: |-
                B = Buy Order
                S = Sell Order
            type: block('alpha', 21, 1)
          - id: shares
            doc: Number of shares being added to the book (may be less than the number of shares entered).
            type: block('numeric', 22, 6)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 28, 6)
          - id: price
            doc: The limit order price
            type: block('price', 34, 10)
          - id: display
            doc: Y = The order is aggregated in the Cboe SIP quote.
            type: block('alpha', 44, 1)
    auction_update_message:
        doc: >-
            Auction Update messages are used to disseminate Cboe price and size
            information during auctions for Cboe listed securities. The Auction Update
            messages are sent every five seconds during a Halt/IPO Quote-Only period.
            Opening Auction Update messages are disseminated every five seconds
            between 9:28 and 9:30 a.m. Closing Auction Update messages are distributed
            every five seconds between 3:55 and 4:00 p.m.

            Cboe Auction Update messages support the Cboe Opening, Closing, Halt and
            IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction
            Process specification for more information on Cboe Auctions.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Auction Update message
            type: block('alpha', 8, 1)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 9, 8)
          - id: auction_type
            doc: |-
                O = Opening Auction
                C = Closing Auction
                H = Halt Auction
                I = IPO Auction
            type: block('alpha', 17, 1)
          - id: reference_price
            doc: BBO Collared auction price (see Auction Process Spec).
            type: block('price', 18, 10)
          - id: buy_shares
            doc: Number of shares on the buy side at the Reference Price.
            type: block('numeric', 28, 10)
          - id: sell_shares
            doc: Number of shares on the sell side at the Reference Price.
            type: block('numeric', 38, 10)
          - id: indicative_price
            doc: Price at which the auction book and the continuous book would match.
            type: block('price', 48, 10)
          - id: auction_only_price
            doc: >-
                Price at which the auction book would match using only Eligible
                Auction Orders (see Auction Process Spec).
            type: block('price', 58, 10)
    trade_message_short:
        doc: >-
            The Trade message provides information about executions of non-displayed
            orders or shares on the Cboe book and routed orders. Trade messages are
            necessary to calculate Cboe execution based data. Trade messages do not
            alter the book and can be ignored if you are just building a book.

            No Add Order message is sent for non-displayed and routed orders, and
            thus, no modify order messages may be sent when non-displayed orders are
            executed. Instead, a Trade message is sent whenever a hidden or routed
            order is executed in whole or in part. A Trade message is also sent when
            there is an execution against any non-displayed portion of a reserve
            order. As with visible orders, hidden orders may be executed in parts. A
            complete view of all Cboe executions can be built by combining all Order
            Executed messages and Trade messages.

            The OrderID of a non-displayed order is obfuscated by default in the Trade
            message, but may be optionally disseminated for a member’s own orders upon
            request. As such, partial executions against the same hidden order will by
            default have different OrderIDs.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Trade message (short)
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Obfuscated Order ID or Order ID of the executed order
            type: block('base_36_numeric', 9, 12)
          - id: side_indicator
            doc: Always B = Buy Order regardless of side of resting order
            type: block('alpha', 21, 1)
          - id: shares
            doc: Incremental Number of shares executed
            type: block('numeric', 22, 6)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 28, 6)
          - id: price
            doc: The execution price of the order
            type: block('price', 34, 10)
          - id: execution_id
            doc: >-
                Cboe generated day-unique execution identifier of this trade.
                Execution ID is also referenced in the Trade Break message.
            type: block('base_36_numeric', 44, 12)
    retail_price_improvement_message:
        doc: >-
            The Retail Price Improvement message is only available on the BYX
            Exchange. This message is a Retail Liquidity Indicator (RLI) that includes
            symbol and side, but not price and size. An RLI will be disseminated when
            there is a Retail Price Improving (RPI) order present for a symbol on the
            BYX Exchange order book OR to indicate a RPI order is no longer available.
            RPI orders offer price improvement in increments of $.001 to Retail Member
            Organizations.
        seq:
          - id: timestamp
            doc: TimeStamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Retail Price Improvement message
            type: block('alpha', 8, 1)
          - id: stock_symbol
            doc: Symbol
            type: block('printable_ascii', 9, 8)
          - id: retail_price_improvement
            doc: |-
                B = Buy Side RPI
                S = Sell Side RPI
                A = Buy & Sell RPI
                N = No RPI
            type: block('alpha', 17, 1)
    trade_message_long:
        doc: >-
            The Trade message provides information about executions of non-displayed
            orders or shares on the Cboe book and routed orders. Trade messages are
            necessary to calculate Cboe execution based data. Trade messages do not
            alter the book and can be ignored if you are just building a book.

            No Add Order message is sent for non-displayed and routed orders, and
            thus, no modify order messages may be sent when non-displayed orders are
            executed. Instead, a Trade message is sent whenever a hidden or routed
            order is executed in whole or in part. A Trade message is also sent when
            there is an execution against any non-displayed portion of a reserve
            order. As with visible orders, hidden orders may be executed in parts. A
            complete view of all Cboe executions can be built by combining all Order
            Executed messages and Trade messages.

            The OrderID of a non-displayed order is obfuscated by default in the Trade
            message, but may be optionally disseminated for a member’s own orders upon
            request. As such, partial executions against the same hidden order will by
            default have different OrderIDs.

            NOTE: The long version of the Trade message has been made available to
            accommodate larger symbol sizes possible through the ISRA plan.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Trade message (long)
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Obfuscated Order ID or Order ID of the executed order.
            type: block('base_36_numeric', 9, 12)
          - id: side_indicator
            doc: Always B = Buy Order regardless of side of resting order
            type: block('alpha', 21, 1)
          - id: shares
            doc: Incremental Number of shares executed
            type: block('numeric', 22, 6)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 28, 8)
          - id: price
            doc: The execution price of the order
            type: block('price', 36, 10)
          - id: execution_id
            doc: >-
                Cboe generated day-unique execution identifier of this trade.
                Execution ID is also referenced in the Trade Break message.
            type: block('base_36_numeric', 46, 12)
    order_executed_message:
        doc: >-
            Order Executed messages are sent when a visible order on the Cboe book is
            executed in whole or in part. The execution price equals the limit order
            price found in the original Add Order message.

            NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously
            sent with an Add Order message. Multiple Order Modification messages may
            modify a single order and the effects are cumulative. Order Modification
            messages always reduce the remaining shares in the referenced open order
            by the number of shares indicated. When the remaining shares for an order
            reach zero, the order is dead and should be removed from the book.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Order Executed message
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Order ID of a previously sent Add Order Message that was executed.
            type: block('base_36_numeric', 9, 12)
          - id: executed_shares
            doc: Number of shares executed
            type: block('numeric', 21, 6)
          - id: execution_id
            doc: >-
                Cboe generated day-unique execution identifier of this execution.
                Execution ID is also referenced in the Trade Break Message.
            type: block('base_36_numeric', 27, 12)
    add_order_message_long:
        doc: >-
            An Add Order message represents a newly accepted visible order on the Cboe
            book. It includes a day-specific Order ID assigned by Cboe to the order.
            The Display field is used to reflect whether or not the order can be
            considered a protected quote and thus reportable to the SIP.

            The long version of the Add Order message has been made available to
            accommodate larger symbol sizes possible through the ISRA plan.

            NOTE: If an order’s Price or Display values change within the Cboe
            matching engine, a Cancel Order Message will be immediately followed by a
            new Add Order message with the same Order ID as the original order. An
            order that changes its Display value from “N” to “Y” will not lose its
            priority.
        seq:
          - id: timestamp
            doc: Timestamp
            type: block('timestamp', 0, 8)
          - id: message_type
            doc: Add Order message (long)
            type: block('alpha', 8, 1)
          - id: order_id
            doc: Day-specific identifier assigned to this order
            type: block('base_36_numeric', 9, 12)
          - id: side_indicator
            doc: |-
                B = Buy Order
                S = Sell Order
            type: block('alpha', 21, 1)
          - id: shares
            doc: >-
                Number of shares being added to the book (may be less than the
                number of shares entered).
            type: block('numeric', 22, 6)
          - id: stock_symbol
            doc: Stock symbol right padded with spaces.
            type: block('printable_ascii', 28, 8)
          - id: price
            doc: The limit order price
            type: block('price', 36, 10)
          - id: display
            doc: Y = The order is aggregated in the Cboe SIP quote.
            type: block('alpha', 46, 1)
          - id: participantid
            doc: >-
                Optionally specified. If specified, MPID or RTAL for  retail
                specified orders (equities) of firm attributed to this quote. Space
                filled otherwise.
            type: block('alpha', 47, 4)
