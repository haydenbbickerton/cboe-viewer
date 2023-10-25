// This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(['kaitai-struct/KaitaiStream'], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory(require('kaitai-struct/KaitaiStream'));
  } else {
    root.Cboe = factory(root.KaitaiStream);
  }
}(this, function (KaitaiStream) {
var Cboe = (function() {
  function Cboe(_io, _parent, _root) {
    this._io = _io;
    this._parent = _parent;
    this._root = _root || this;

    this._read();
  }
  Cboe.prototype._read = function() {
    this.records = [];
    var i = 0;
    while (!this._io.isEof()) {
      this.records.push(new Record(this._io, this, this._root, i, this._io.pos));
      i++;
    }
  }

  /**
   * Order Cancel messages are sent when a visible order on the Cboe book is canceled in whole or in part.
   * NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously sent with an Add Order message. Multiple Order Modification messages may modify a single order and the effects are cumulative. Order Modification messages always reduce the remaining shares in the referenced open order by the number of shares indicated. When the remaining shares for an order reach zero, the order is dead and should be removed from the book.
   */

  var OrderCancelMessage = Cboe.OrderCancelMessage = (function() {
    function OrderCancelMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    OrderCancelMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.canceledShares = new Block(this._io, this, this._root, "numeric", 21, 6);
    }

    /**
     * Timestamp
     */

    /**
     * Order Cancel message
     */

    /**
     * Order ID of a previously sent Add Order Message that has been reduced or cancelled
     */

    /**
     * Number of shares canceled
     */

    return OrderCancelMessage;
  })();

  /**
   * The Retail Price Improvement message is only available on the BYX Exchange. This message is a Retail Liquidity Indicator (RLI) that includes symbol and side, but not price and size. An RLI will be disseminated when there is a Retail Price Improving (RPI) order present for a symbol on the BYX Exchange order book OR to indicate a RPI order is no longer available. RPI orders offer price improvement in increments of $.001 to Retail Member Organizations.
   */

  var RetailPriceImprovementMessage = Cboe.RetailPriceImprovementMessage = (function() {
    function RetailPriceImprovementMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    RetailPriceImprovementMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 9, 8);
      this.retailPriceImprovement = new Block(this._io, this, this._root, "alpha", 17, 1);
    }

    /**
     * TimeStamp
     */

    /**
     * Retail Price Improvement message
     */

    /**
     * Symbol
     */

    /**
     * B = Buy Side RPI
     * S = Sell Side RPI
     * A = Buy & Sell RPI
     * N = No RPI
     */

    return RetailPriceImprovementMessage;
  })();

  /**
   * Order Executed messages are sent when a visible order on the Cboe book is executed in whole or in part. The execution price equals the limit order price found in the original Add Order message.
   * NOTE:  Order Modification messages (4.4.x) refer to an Order ID previously sent with an Add Order message. Multiple Order Modification messages may modify a single order and the effects are cumulative. Order Modification messages always reduce the remaining shares in the referenced open order by the number of shares indicated. When the remaining shares for an order reach zero, the order is dead and should be removed from the book.
   */

  var OrderExecutedMessage = Cboe.OrderExecutedMessage = (function() {
    function OrderExecutedMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    OrderExecutedMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.executedShares = new Block(this._io, this, this._root, "numeric", 21, 6);
      this.executionId = new Block(this._io, this, this._root, "base_36_numeric", 27, 12);
    }

    /**
     * Timestamp
     */

    /**
     * Order Executed message
     */

    /**
     * Order ID of a previously sent Add Order Message that was executed.
     */

    /**
     * Number of shares executed
     */

    /**
     * Cboe generated day-unique execution identifier of this execution. Execution ID is also referenced in the Trade Break Message.
     */

    return OrderExecutedMessage;
  })();

  /**
   * The Trade message provides information about executions of non-displayed orders or shares on the Cboe book and routed orders. Trade messages are necessary to calculate Cboe execution based data. Trade messages do not alter the book and can be ignored if you are just building a book.
   * No Add Order message is sent for non-displayed and routed orders, and thus, no modify order messages may be sent when non-displayed orders are executed. Instead, a Trade message is sent whenever a hidden or routed order is executed in whole or in part. A Trade message is also sent when there is an execution against any non-displayed portion of a reserve order. As with visible orders, hidden orders may be executed in parts. A complete view of all Cboe executions can be built by combining all Order Executed messages and Trade messages.
   * The OrderID of a non-displayed order is obfuscated by default in the Trade message, but may be optionally disseminated for a member’s own orders upon request. As such, partial executions against the same hidden order will by default have different OrderIDs.
   */

  var TradeMessageShort = Cboe.TradeMessageShort = (function() {
    function TradeMessageShort(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    TradeMessageShort.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.sideIndicator = new Block(this._io, this, this._root, "alpha", 21, 1);
      this.shares = new Block(this._io, this, this._root, "numeric", 22, 6);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 28, 6);
      this.price = new Block(this._io, this, this._root, "price", 34, 10);
      this.executionId = new Block(this._io, this, this._root, "base_36_numeric", 44, 12);
    }

    /**
     * Timestamp
     */

    /**
     * Trade message (short)
     */

    /**
     * Obfuscated Order ID or Order ID of the executed order
     */

    /**
     * Always B = Buy Order regardless of side of resting order
     */

    /**
     * Incremental Number of shares executed
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * The execution price of the order
     */

    /**
     * Cboe generated day-unique execution identifier of this trade. Execution ID is also referenced in the Trade Break message.
     */

    return TradeMessageShort;
  })();

  /**
   * The Trade message provides information about executions of non-displayed orders or shares on the Cboe book and routed orders. Trade messages are necessary to calculate Cboe execution based data. Trade messages do not alter the book and can be ignored if you are just building a book.
   * No Add Order message is sent for non-displayed and routed orders, and thus, no modify order messages may be sent when non-displayed orders are executed. Instead, a Trade message is sent whenever a hidden or routed order is executed in whole or in part. A Trade message is also sent when there is an execution against any non-displayed portion of a reserve order. As with visible orders, hidden orders may be executed in parts. A complete view of all Cboe executions can be built by combining all Order Executed messages and Trade messages.
   * The OrderID of a non-displayed order is obfuscated by default in the Trade message, but may be optionally disseminated for a member’s own orders upon request. As such, partial executions against the same hidden order will by default have different OrderIDs.
   * NOTE: The long version of the Trade message has been made available to accommodate larger symbol sizes possible through the ISRA plan.
   */

  var TradeMessageLong = Cboe.TradeMessageLong = (function() {
    function TradeMessageLong(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    TradeMessageLong.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.sideIndicator = new Block(this._io, this, this._root, "alpha", 21, 1);
      this.shares = new Block(this._io, this, this._root, "numeric", 22, 6);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 28, 8);
      this.price = new Block(this._io, this, this._root, "price", 36, 10);
      this.executionId = new Block(this._io, this, this._root, "base_36_numeric", 46, 12);
    }

    /**
     * Timestamp
     */

    /**
     * Trade message (long)
     */

    /**
     * Obfuscated Order ID or Order ID of the executed order.
     */

    /**
     * Always B = Buy Order regardless of side of resting order
     */

    /**
     * Incremental Number of shares executed
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * The execution price of the order
     */

    /**
     * Cboe generated day-unique execution identifier of this trade. Execution ID is also referenced in the Trade Break message.
     */

    return TradeMessageLong;
  })();

  /**
   * Auction Summary messages are used to disseminate the results of an auction of a Cboe listed security. An Opening Auction Summary message for each Cboe listed security is sent at the conclusion of its opening auction at 9:30 a.m. and represents the Cboe official opening price. A Closing Auction Summary message for each Cboe listed security is sent at the conclusion of its closing auction at 4:00 p.m. and represents the Cboe official closing price. An IPO Auction Summary message for each Cboe listed security is sent at the conclusion of the IPO Auction and represents the official Cboe IPO opening price.
   * Cboe Auction Summary messages support the Cboe Opening, Closing, Halt and IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction Process specification for more information on Cboe Auctions.
   */

  var AuctionSummaryMessage = Cboe.AuctionSummaryMessage = (function() {
    function AuctionSummaryMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    AuctionSummaryMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 9, 8);
      this.auctionType = new Block(this._io, this, this._root, "alpha", 17, 1);
      this.price = new Block(this._io, this, this._root, "price", 18, 10);
      this.shares = new Block(this._io, this, this._root, "numeric", 28, 10);
    }

    /**
     * Timestamp
     */

    /**
     * Auction Summary message
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * O = Opening Auction
     * C = Closing Auction
     * H = Halt Auction
     * I = IPO Auction
     */

    /**
     * Auction price
     */

    /**
     * Cumulative number of shares  executed during the auction
     */

    return AuctionSummaryMessage;
  })();

  /**
   * An Add Order message represents a newly accepted visible order on the Cboe book. It includes a day-specific Order ID assigned by Cboe to the order. The Display field is used to reflect whether or not the order can be considered a protected quote and thus reportable to the SIP.
   * NOTE: If an order’s Price or Display values change within the Cboe matching engine, a Cancel Order Message will be immediately followed by a new Add Order message with the same Order ID as the original order. An order that changes its Display value from “N” to “Y” will not lose its priority.
   */

  var AddOrderMessageShort = Cboe.AddOrderMessageShort = (function() {
    function AddOrderMessageShort(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    AddOrderMessageShort.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.sideIndicator = new Block(this._io, this, this._root, "alpha", 21, 1);
      this.shares = new Block(this._io, this, this._root, "numeric", 22, 6);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 28, 6);
      this.price = new Block(this._io, this, this._root, "price", 34, 10);
      this.display = new Block(this._io, this, this._root, "alpha", 44, 1);
    }

    /**
     * Timestamp
     */

    /**
     * Add Order message (short)
     */

    /**
     * Day-specific identifier assigned to this order
     */

    /**
     * B = Buy Order
     * S = Sell Order
     */

    /**
     * Number of shares being added to the book (may be less than the number of shares entered).
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * The limit order price
     */

    /**
     * Y = The order is aggregated in the Cboe SIP quote.
     */

    return AddOrderMessageShort;
  })();

  /**
   * The Trading Status message is used to indicate the current trading status of a security. A Trading Status message will be sent whenever a security’s trading status changes. In addition, Cboe will send a Trading Status message for all securities that are “Halted” or have a price test in effect before the start of trading hours.
   * Trading Status of `S` will be implied at system startup. `T` will be sent as securities are available for trading. `A` will be distributed when orders can be accepted for queuing in preparation for the market open.
   */

  var TradingStatusMessage = Cboe.TradingStatusMessage = (function() {
    function TradingStatusMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    TradingStatusMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 9, 8);
      this.haltStatus = new Block(this._io, this, this._root, "alpha", 17, 1);
      this.regShoAction = new Block(this._io, this, this._root, "numeric", 18, 1);
      this.reserved1 = new Block(this._io, this, this._root, "alpha", 19, 1);
      this.reserved2 = new Block(this._io, this, this._root, "alpha", 20, 1);
    }

    /**
     * Timestamp
     */

    /**
     * Trading Status message
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * A = Accepting Orders for Queuing
     * H = Halted
     * Q = Quote-Only (Cboe Listings)
     * S = Exchange Specific Suspension
     * T = Trading
     */

    /**
     * 0 = No price test in effect
     * 1 = Reg SHO price test restriction in effect
     */

    /**
     * Reserved
     */

    /**
     * Reserved
     */

    return TradingStatusMessage;
  })();

  /**
   * An Add Order message represents a newly accepted visible order on the Cboe book. It includes a day-specific Order ID assigned by Cboe to the order. The Display field is used to reflect whether or not the order can be considered a protected quote and thus reportable to the SIP.
   * The long version of the Add Order message has been made available to accommodate larger symbol sizes possible through the ISRA plan.
   * NOTE: If an order’s Price or Display values change within the Cboe matching engine, a Cancel Order Message will be immediately followed by a new Add Order message with the same Order ID as the original order. An order that changes its Display value from “N” to “Y” will not lose its priority.
   */

  var AddOrderMessageLong = Cboe.AddOrderMessageLong = (function() {
    function AddOrderMessageLong(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    AddOrderMessageLong.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.orderId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
      this.sideIndicator = new Block(this._io, this, this._root, "alpha", 21, 1);
      this.shares = new Block(this._io, this, this._root, "numeric", 22, 6);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 28, 8);
      this.price = new Block(this._io, this, this._root, "price", 36, 10);
      this.display = new Block(this._io, this, this._root, "alpha", 46, 1);
      this.participantid = new Block(this._io, this, this._root, "alpha", 47, 4);
    }

    /**
     * Timestamp
     */

    /**
     * Add Order message (long)
     */

    /**
     * Day-specific identifier assigned to this order
     */

    /**
     * B = Buy Order
     * S = Sell Order
     */

    /**
     * Number of shares being added to the book (may be less than the number of shares entered).
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * The limit order price
     */

    /**
     * Y = The order is aggregated in the Cboe SIP quote.
     */

    /**
     * Optionally specified. If specified, MPID or RTAL for  retail specified orders (equities) of firm attributed to this quote. Space filled otherwise.
     */

    return AddOrderMessageLong;
  })();

  var Block = Cboe.Block = (function() {
    function Block(_io, _parent, _root, type, offset, length) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this.type = type;
      this.offset = offset;
      this.length = length;

      this._read();
    }
    Block.prototype._read = function() {
      this.value = KaitaiStream.bytesToStr(KaitaiStream.bytesTerminate(this._io.readBytes(this.length), 0, false), "ASCII");
    }

    return Block;
  })();

  /**
   * Auction Update messages are used to disseminate Cboe price and size information during auctions for Cboe listed securities. The Auction Update messages are sent every five seconds during a Halt/IPO Quote-Only period. Opening Auction Update messages are disseminated every five seconds between 9:28 and 9:30 a.m. Closing Auction Update messages are distributed every five seconds between 3:55 and 4:00 p.m.
   * Cboe Auction Update messages support the Cboe Opening, Closing, Halt and IPO Auctions on the BZX Exchange. Refer to the Cboe US Equities Auction Process specification for more information on Cboe Auctions.
   */

  var AuctionUpdateMessage = Cboe.AuctionUpdateMessage = (function() {
    function AuctionUpdateMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    AuctionUpdateMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 9, 8);
      this.auctionType = new Block(this._io, this, this._root, "alpha", 17, 1);
      this.referencePrice = new Block(this._io, this, this._root, "price", 18, 10);
      this.buyShares = new Block(this._io, this, this._root, "numeric", 28, 10);
      this.sellShares = new Block(this._io, this, this._root, "numeric", 38, 10);
      this.indicativePrice = new Block(this._io, this, this._root, "price", 48, 10);
      this.auctionOnlyPrice = new Block(this._io, this, this._root, "price", 58, 10);
    }

    /**
     * Timestamp
     */

    /**
     * Auction Update message
     */

    /**
     * Stock symbol right padded with spaces.
     */

    /**
     * O = Opening Auction
     * C = Closing Auction
     * H = Halt Auction
     * I = IPO Auction
     */

    /**
     * BBO Collared auction price (see Auction Process Spec).
     */

    /**
     * Number of shares on the buy side at the Reference Price.
     */

    /**
     * Number of shares on the sell side at the Reference Price.
     */

    /**
     * Price at which the auction book and the continuous book would match.
     */

    /**
     * Price at which the auction book would match using only Eligible Auction Orders (see Auction Process Spec).
     */

    return AuctionUpdateMessage;
  })();

  /**
   * The Symbol Clear message instructs feed recipients to clear all orders for the Cboe book in the specified symbol. This message will be sent at startup each day. It would also be distributed in certain recovery events such as a data center fail-over.
   */

  var SymbolClearMessage = Cboe.SymbolClearMessage = (function() {
    function SymbolClearMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    SymbolClearMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.stockSymbol = new Block(this._io, this, this._root, "printable_ascii", 9, 8);
    }

    /**
     * TimeStamp
     */

    /**
     * Symbol Clear Message
     */

    /**
     * Stock symbol right padded with spaces.
     */

    return SymbolClearMessage;
  })();

  /**
   * The Trade Break message is sent whenever an execution on Cboe is broken. Trade breaks are rare and only affect applications that rely upon Cboe execution based data. Applications that simply build a Cboe book can ignore Trade Break messages.
   */

  var TradeBreakMessage = Cboe.TradeBreakMessage = (function() {
    function TradeBreakMessage(_io, _parent, _root) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;

      this._read();
    }
    TradeBreakMessage.prototype._read = function() {
      this.timestamp = new Block(this._io, this, this._root, "timestamp", 0, 8);
      this.messageType = new Block(this._io, this, this._root, "alpha", 8, 1);
      this.executionId = new Block(this._io, this, this._root, "base_36_numeric", 9, 12);
    }

    /**
     * Timestamp
     */

    /**
     * Trade Break message
     */

    /**
     * Cboe execution identifier of the execution that was broken. Execution ID refers to previously sent Order Execution or Trade message.
     */

    return TradeBreakMessage;
  })();

  var Record = Cboe.Record = (function() {
    function Record(_io, _parent, _root, idx, ofs) {
      this._io = _io;
      this._parent = _parent;
      this._root = _root || this;
      this.idx = idx;
      this.ofs = ofs;

      this._read();
    }
    Record.prototype._read = function() {
      this.startOfLine = this._io.ensureFixedContents([83]);
      this.raw = KaitaiStream.bytesToStr(this._io.readBytesTerm(13, false, false, true), "ASCII");
      this.endOfLine = this._io.ensureFixedContents([13, 10]);
    }
    Object.defineProperty(Record.prototype, 'typeIndicator', {
      get: function() {
        if (this._m_typeIndicator !== undefined)
          return this._m_typeIndicator;
        var io = this._root._io;
        var _pos = io.pos;
        io.seek((this.dataOffset + this._root.recordTypeMask));
        this._m_typeIndicator = KaitaiStream.bytesToStr(io.readBytes(1), "ASCII");
        io.seek(_pos);
        return this._m_typeIndicator;
      }
    });
    Object.defineProperty(Record.prototype, 'data', {
      get: function() {
        if (this._m_data !== undefined)
          return this._m_data;
        var io = this._root._io;
        var _pos = io.pos;
        io.seek(this.dataOffset);
        switch (this.typeIndicator) {
        case "I":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new AuctionUpdateMessage(_io__raw__m_data, this, this._root);
          break;
        case "d":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new AddOrderMessageLong(_io__raw__m_data, this, this._root);
          break;
        case "s":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new SymbolClearMessage(_io__raw__m_data, this, this._root);
          break;
        case "B":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new TradeBreakMessage(_io__raw__m_data, this, this._root);
          break;
        case "E":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new OrderExecutedMessage(_io__raw__m_data, this, this._root);
          break;
        case "X":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new OrderCancelMessage(_io__raw__m_data, this, this._root);
          break;
        case "R":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new RetailPriceImprovementMessage(_io__raw__m_data, this, this._root);
          break;
        case "r":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new TradeMessageLong(_io__raw__m_data, this, this._root);
          break;
        case "A":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new AddOrderMessageShort(_io__raw__m_data, this, this._root);
          break;
        case "H":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new TradingStatusMessage(_io__raw__m_data, this, this._root);
          break;
        case "J":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new AuctionSummaryMessage(_io__raw__m_data, this, this._root);
          break;
        case "P":
          this._raw__m_data = io.readBytes(this.dataSize);
          var _io__raw__m_data = new KaitaiStream(this._raw__m_data);
          this._m_data = new TradeMessageShort(_io__raw__m_data, this, this._root);
          break;
        default:
          this._m_data = io.readBytes(this.dataSize);
          break;
        }
        io.seek(_pos);
        return this._m_data;
      }
    });
    Object.defineProperty(Record.prototype, 'dataOffset', {
      get: function() {
        if (this._m_dataOffset !== undefined)
          return this._m_dataOffset;
        this._m_dataOffset = (this.ofs + 1);
        return this._m_dataOffset;
      }
    });
    Object.defineProperty(Record.prototype, 'dataSize', {
      get: function() {
        if (this._m_dataSize !== undefined)
          return this._m_dataSize;
        this._m_dataSize = this.raw.length;
        return this._m_dataSize;
      }
    });

    /**
     * Magic starting char "S"
     */

    return Record;
  })();
  Object.defineProperty(Cboe.prototype, 'numRecordEntries', {
    get: function() {
      if (this._m_numRecordEntries !== undefined)
        return this._m_numRecordEntries;
      this._m_numRecordEntries = this.records.length;
      return this._m_numRecordEntries;
    }
  });

  /**
   * Magic number to offset the position of the msgtype char in record.
   */
  Object.defineProperty(Cboe.prototype, 'recordTypeMask', {
    get: function() {
      if (this._m_recordTypeMask !== undefined)
        return this._m_recordTypeMask;
      this._m_recordTypeMask = 8;
      return this._m_recordTypeMask;
    }
  });

  return Cboe;
})();
return Cboe;
}));
