# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Cboe(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(self._root.Record(i, self._io.pos(), self._io, self, self._root))
            i += 1


    class OrderCancelMessage(KaitaiStruct):
        """Order Cancel messages are sent when a visible order on the Cboe book is canceled in whole or in part.
        NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously sent with an Add Order message. Multiple Order Modification messages may modify a single order and the effects are cumulative. Order Modification messages always reduce the remaining shares in the referenced open order by the number of shares indicated. When the remaining shares for an order reach zero, the order is dead and should be removed from the book."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.canceled_shares = self._root.Block(u"numeric", 21, 6, self._io, self, self._root)


    class RetailPriceImprovementMessage(KaitaiStruct):
        """The Retail Price Improvement message is only available on the BYX Exchange. This message is a Retail Liquidity Indicator (RLI) that includes symbol and side, but not price and size. An RLI will be disseminated when there is a Retail Price Improving (RPI) order present for a symbol on the BYX Exchange order book OR to indicate a RPI order is no longer available. RPI orders offer price improvement in increments of $.001 to Retail Member Organizations."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 9, 8, self._io, self, self._root)
            self.retail_price_improvement = self._root.Block(u"alpha", 17, 1, self._io, self, self._root)


    class OrderExecutedMessage(KaitaiStruct):
        """Order Executed messages are sent when a visible order on the Cboe book is executed in whole or in part. The execution price equals the limit order price found in the original Add Order message.
        NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously sent with an Add Order message. Multiple Order Modification messages may modify a single order and the effects are cumulative. Order Modification messages always reduce the remaining shares in the referenced open order by the number of shares indicated. When the remaining shares for an order reach zero, the order is dead and should be removed from the book."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.executed_shares = self._root.Block(u"numeric", 21, 6, self._io, self, self._root)
            self.execution_id = self._root.Block(u"base_36_numeric", 27, 12, self._io, self, self._root)


    class TradeMessageShort(KaitaiStruct):
        """The Trade message provides information about executions of non-displayed orders or shares on the Cboe book and routed orders. Trade messages are necessary to calculate Cboe execution based data. Trade messages do not alter the book and can be ignored if you are just building a book.
        No Add Order message is sent for non-displayed and routed orders, and thus, no modify order messages may be sent when non-displayed orders are executed. Instead, a Trade message is sent whenever a hidden or routed order is executed in whole or in part. A Trade message is also sent when there is an execution against any non-displayed portion of a reserve order. As with visible orders, hidden orders may be executed in parts. A complete view of all Cboe executions can be built by combining all Order Executed messages and Trade messages.
        The OrderID of a non-displayed order is obfuscated by default in the Trade message, but may be optionally disseminated for a member’s own orders upon request. As such, partial executions against the same hidden order will by default have different OrderIDs."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.side_indicator = self._root.Block(u"alpha", 21, 1, self._io, self, self._root)
            self.shares = self._root.Block(u"numeric", 22, 6, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 28, 6, self._io, self, self._root)
            self.price = self._root.Block(u"price", 34, 10, self._io, self, self._root)
            self.execution_id = self._root.Block(u"base_36_numeric", 44, 12, self._io, self, self._root)


    class TradeMessageLong(KaitaiStruct):
        """The Trade message provides information about executions of non-displayed orders or shares on the Cboe book and routed orders. Trade messages are necessary to calculate Cboe execution based data. Trade messages do not alter the book and can be ignored if you are just building a book.
        No Add Order message is sent for non-displayed and routed orders, and thus, no modify order messages may be sent when non-displayed orders are executed. Instead, a Trade message is sent whenever a hidden or routed order is executed in whole or in part. A Trade message is also sent when there is an execution against any non-displayed portion of a reserve order. As with visible orders, hidden orders may be executed in parts. A complete view of all Cboe executions can be built by combining all Order Executed messages and Trade messages.
        The OrderID of a non-displayed order is obfuscated by default in the Trade message, but may be optionally disseminated for a member’s own orders upon request. As such, partial executions against the same hidden order will by default have different OrderIDs.
        NOTE: The long version of the Trade message has been made available to accommodate larger symbol sizes possible through the ISRA plan."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.side_indicator = self._root.Block(u"alpha", 21, 1, self._io, self, self._root)
            self.shares = self._root.Block(u"numeric", 22, 6, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 28, 8, self._io, self, self._root)
            self.price = self._root.Block(u"price", 36, 10, self._io, self, self._root)
            self.execution_id = self._root.Block(u"base_36_numeric", 46, 12, self._io, self, self._root)


    class AuctionSummaryMessage(KaitaiStruct):
        """Auction Summary messages are used to disseminate the results of an auction of a Cboe listed security. An Opening Auction Summary message for each Cboe listed security is sent at the conclusion of its opening auction at 9:30 a.m. and represents the Cboe official opening price. A Closing Auction Summary message for each Cboe listed security is sent at the conclusion of its closing auction at 4:00 p.m. and represents the Cboe official closing price. An IPO Auction Summary message for each Cboe listed security is sent at the conclusion of the IPO Auction and represents the official Cboe IPO opening price.
        Cboe Auction Summary messages support the Cboe Opening, Closing, Halt and IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction Process specification for more information on Cboe Auctions."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 9, 8, self._io, self, self._root)
            self.auction_type = self._root.Block(u"alpha", 17, 1, self._io, self, self._root)
            self.price = self._root.Block(u"price", 18, 10, self._io, self, self._root)
            self.shares = self._root.Block(u"numeric", 28, 10, self._io, self, self._root)


    class AddOrderMessageShort(KaitaiStruct):
        """An Add Order message represents a newly accepted visible order on the Cboe book. It includes a day-specific Order ID assigned by Cboe to the order. The Display field is used to reflect whether or not the order can be considered a protected quote and thus reportable to the SIP.
        NOTE: If an order’s Price or Display values change within the Cboe matching engine, a Cancel Order Message will be immediately followed by a new Add Order message with the same Order ID as the original order. An order that changes its Display value from “N” to “Y” will not lose its priority."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.side_indicator = self._root.Block(u"alpha", 21, 1, self._io, self, self._root)
            self.shares = self._root.Block(u"numeric", 22, 6, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 28, 6, self._io, self, self._root)
            self.price = self._root.Block(u"price", 34, 10, self._io, self, self._root)
            self.display = self._root.Block(u"alpha", 44, 1, self._io, self, self._root)


    class TradingStatusMessage(KaitaiStruct):
        """The Trading Status message is used to indicate the current trading status of a security. A Trading Status message will be sent whenever a security’s trading status changes. In addition, Cboe will send a Trading Status message for all securities that are “Halted” or have a price test in effect before the start of trading hours.
        Trading Status of `S` will be implied at system startup. `T` will be sent as securities are available for trading. `A` will be distributed when orders can be accepted for queuing in preparation for the market open."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 9, 8, self._io, self, self._root)
            self.halt_status = self._root.Block(u"alpha", 17, 1, self._io, self, self._root)
            self.reg_sho_action = self._root.Block(u"numeric", 18, 1, self._io, self, self._root)
            self.reserved1 = self._root.Block(u"alpha", 19, 1, self._io, self, self._root)
            self.reserved2 = self._root.Block(u"alpha", 20, 1, self._io, self, self._root)


    class AddOrderMessageLong(KaitaiStruct):
        """An Add Order message represents a newly accepted visible order on the Cboe book. It includes a day-specific Order ID assigned by Cboe to the order. The Display field is used to reflect whether or not the order can be considered a protected quote and thus reportable to the SIP.
        The long version of the Add Order message has been made available to accommodate larger symbol sizes possible through the ISRA plan.
        NOTE: If an order’s Price or Display values change within the Cboe matching engine, a Cancel Order Message will be immediately followed by a new Add Order message with the same Order ID as the original order. An order that changes its Display value from “N” to “Y” will not lose its priority."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.order_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)
            self.side_indicator = self._root.Block(u"alpha", 21, 1, self._io, self, self._root)
            self.shares = self._root.Block(u"numeric", 22, 6, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 28, 8, self._io, self, self._root)
            self.price = self._root.Block(u"price", 36, 10, self._io, self, self._root)
            self.display = self._root.Block(u"alpha", 46, 1, self._io, self, self._root)
            self.participantid = self._root.Block(u"alpha", 47, 4, self._io, self, self._root)


    class Block(KaitaiStruct):
        def __init__(self, type, offset, length, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = type
            self.offset = offset
            self.length = length
            self._read()

        def _read(self):
            self.value = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.length), 0, False)).decode(u"ASCII")


    class AuctionUpdateMessage(KaitaiStruct):
        """Auction Update messages are used to disseminate Cboe price and size information during auctions for Cboe listed securities. The Auction Update messages are sent every five seconds during a Halt/IPO Quote-Only period. Opening Auction Update messages are disseminated every five seconds between 9:28 and 9:30 a.m. Closing Auction Update messages are distributed every five seconds between 3:55 and 4:00 p.m.
        Cboe Auction Update messages support the Cboe Opening, Closing, Halt and IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction Process specification for more information on Cboe Auctions."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 9, 8, self._io, self, self._root)
            self.auction_type = self._root.Block(u"alpha", 17, 1, self._io, self, self._root)
            self.reference_price = self._root.Block(u"price", 18, 10, self._io, self, self._root)
            self.buy_shares = self._root.Block(u"numeric", 28, 10, self._io, self, self._root)
            self.sell_shares = self._root.Block(u"numeric", 38, 10, self._io, self, self._root)
            self.indicative_price = self._root.Block(u"price", 48, 10, self._io, self, self._root)
            self.auction_only_price = self._root.Block(u"price", 58, 10, self._io, self, self._root)


    class SymbolClearMessage(KaitaiStruct):
        """The Symbol Clear message instructs feed recipients to clear all orders for the Cboe book in the specified symbol. This message will be sent at startup each day. It would also be distributed in certain recovery events such as a data center fail-over."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.stock_symbol = self._root.Block(u"printable_ascii", 9, 8, self._io, self, self._root)


    class TradeBreakMessage(KaitaiStruct):
        """The Trade Break message is sent whenever an execution on Cboe is broken. Trade breaks are rare and only affect applications that rely upon Cboe execution based data. Applications that simply build a Cboe book can ignore Trade Break messages."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._root.Block(u"timestamp", 0, 8, self._io, self, self._root)
            self.message_type = self._root.Block(u"alpha", 8, 1, self._io, self, self._root)
            self.execution_id = self._root.Block(u"base_36_numeric", 9, 12, self._io, self, self._root)


    class Record(KaitaiStruct):
        def __init__(self, idx, ofs, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self.ofs = ofs
            self._read()

        def _read(self):
            self.start_of_line = self._io.ensure_fixed_contents(b"\x53")
            self.raw = (self._io.read_bytes_term(13, False, False, True)).decode(u"ASCII")
            self.end_of_line = self._io.ensure_fixed_contents(b"\x0D\x0A")

        @property
        def type_indicator(self):
            if hasattr(self, '_m_type_indicator'):
                return self._m_type_indicator if hasattr(self, '_m_type_indicator') else None

            io = self._root._io
            _pos = io.pos()
            io.seek((self.data_offset + self._root.record_type_mask))
            self._m_type_indicator = (io.read_bytes(1)).decode(u"ASCII")
            io.seek(_pos)
            return self._m_type_indicator if hasattr(self, '_m_type_indicator') else None

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.data_offset)
            _on = self.type_indicator
            if _on == u"I":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.AuctionUpdateMessage(_io__raw__m_data, self, self._root)
            elif _on == u"d":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.AddOrderMessageLong(_io__raw__m_data, self, self._root)
            elif _on == u"s":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.SymbolClearMessage(_io__raw__m_data, self, self._root)
            elif _on == u"B":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.TradeBreakMessage(_io__raw__m_data, self, self._root)
            elif _on == u"E":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.OrderExecutedMessage(_io__raw__m_data, self, self._root)
            elif _on == u"X":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.OrderCancelMessage(_io__raw__m_data, self, self._root)
            elif _on == u"R":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.RetailPriceImprovementMessage(_io__raw__m_data, self, self._root)
            elif _on == u"r":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.TradeMessageLong(_io__raw__m_data, self, self._root)
            elif _on == u"A":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.AddOrderMessageShort(_io__raw__m_data, self, self._root)
            elif _on == u"H":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.TradingStatusMessage(_io__raw__m_data, self, self._root)
            elif _on == u"J":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.AuctionSummaryMessage(_io__raw__m_data, self, self._root)
            elif _on == u"P":
                self._raw__m_data = io.read_bytes(self.data_size)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = self._root.TradeMessageShort(_io__raw__m_data, self, self._root)
            else:
                self._m_data = io.read_bytes(self.data_size)
            io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None

        @property
        def data_offset(self):
            if hasattr(self, '_m_data_offset'):
                return self._m_data_offset if hasattr(self, '_m_data_offset') else None

            self._m_data_offset = (self.ofs + 1)
            return self._m_data_offset if hasattr(self, '_m_data_offset') else None

        @property
        def data_size(self):
            if hasattr(self, '_m_data_size'):
                return self._m_data_size if hasattr(self, '_m_data_size') else None

            self._m_data_size = len(self.raw)
            return self._m_data_size if hasattr(self, '_m_data_size') else None


    @property
    def num_record_entries(self):
        if hasattr(self, '_m_num_record_entries'):
            return self._m_num_record_entries if hasattr(self, '_m_num_record_entries') else None

        self._m_num_record_entries = len(self.records)
        return self._m_num_record_entries if hasattr(self, '_m_num_record_entries') else None

    @property
    def record_type_mask(self):
        """Magic number to offset the position of the msgtype char in record."""
        if hasattr(self, '_m_record_type_mask'):
            return self._m_record_type_mask if hasattr(self, '_m_record_type_mask') else None

        self._m_record_type_mask = 8
        return self._m_record_type_mask if hasattr(self, '_m_record_type_mask') else None


