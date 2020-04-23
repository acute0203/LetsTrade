import MetaTrader5 as mt5
import datetime
from PlatformInterface.PlatformInterface import PlatformInterface

class MT5Platform(PlatformInterface):
    
    _eTimeFrame:dict = {
            "TIMEFRAME_M1":mt5.TIMEFRAME_M1,
            "TIMEFRAME_M2":mt5.TIMEFRAME_M2,
            "TIMEFRAME_M3":mt5.TIMEFRAME_M3,
            "TIMEFRAME_M4":mt5.TIMEFRAME_M4,
            "TIMEFRAME_M5":mt5.TIMEFRAME_M5,
            "TIMEFRAME_M6":mt5.TIMEFRAME_M6,
            "TIMEFRAME_M10":mt5.TIMEFRAME_M10,
            "TIMEFRAME_M12":mt5.TIMEFRAME_M12,
            "TIMEFRAME_M15":mt5.TIMEFRAME_M15,
            "TIMEFRAME_M20":mt5.TIMEFRAME_M20,
            "TIMEFRAME_M30":mt5.TIMEFRAME_M30,
            "TIMEFRAME_H1":mt5.TIMEFRAME_H1,
            "TIMEFRAME_H2":mt5.TIMEFRAME_H2,
            "TIMEFRAME_H3":mt5.TIMEFRAME_H3,
            "TIMEFRAME_H4":mt5.TIMEFRAME_H4,
            "TIMEFRAME_H6":mt5.TIMEFRAME_H6,
            "TIMEFRAME_H8":mt5.TIMEFRAME_H8,
            "TIMEFRAME_H12":mt5.TIMEFRAME_H12,
            "TIMEFRAME_D1":mt5.TIMEFRAME_D1,
            "TIMEFRAME_W1":mt5.TIMEFRAME_W1,
            "TIMEFRAME_M1":mt5.TIMEFRAME_M1
            }

    _eTickFlags:dict = {
            "COPY_TICKS_ALL":mt5.COPY_TICKS_ALL,
            "COPY_TICKS_INFO":mt5.COPY_TICKS_INFO,
            "COPY_TICKS_TRADE":mt5.COPY_TICKS_TRADE
        }
        

    _eOrderType:dict = {
            "ORDER_TYPE_BUY":mt5.ORDER_TYPE_BUY,
            "ORDER_TYPE_SELL":mt5.ORDER_TYPE_SELL,
            "ORDER_TYPE_BUY_LIMIT":mt5.ORDER_TYPE_BUY_LIMIT,
            "ORDER_TYPE_SELL_LIMIT":mt5.ORDER_TYPE_SELL_LIMIT,
            "ORDER_TYPE_BUY_STOP":mt5.ORDER_TYPE_BUY_STOP,
            "ORDER_TYPE_SELL_STOP":mt5.ORDER_TYPE_SELL_STOP,
            "ORDER_TYPE_BUY_STOP_LIMIT":mt5.ORDER_TYPE_BUY_STOP_LIMIT,
            "ORDER_TYPE_SELL_STOP_LIMIT":mt5.ORDER_TYPE_SELL_STOP_LIMIT,
            "ORDER_TYPE_CLOSE_BY":mt5.ORDER_TYPE_CLOSE_BY
        }

    _eTradeRequestActions:dict = {
            "TRADE_ACTION_DEAL":mt5.TRADE_ACTION_DEAL,
            "TRADE_ACTION_PENDING":mt5.TRADE_ACTION_PENDING,
            "TRADE_ACTION_SLTP":mt5.TRADE_ACTION_SLTP,
            "TRADE_ACTION_MODIFY":mt5.TRADE_ACTION_MODIFY,
            "TRADE_ACTION_REMOVE":mt5.TRADE_ACTION_REMOVE,
            "TRADE_ACTION_CLOSE_BY":mt5.TRADE_ACTION_CLOSE_BY
        }

    _eOrderTypeFilling:dict = {
            "ORDER_FILLING_FOK":mt5.ORDER_FILLING_FOK,
            "ORDER_FILLING_IOC":mt5.ORDER_FILLING_IOC,
            "ORDER_FILLING_RETURN":mt5.ORDER_FILLING_RETURN
        }

    _eOrderTypeTime:dict = {
            "ORDER_TIME_GTC":mt5.ORDER_TIME_GTC,
            "ORDER_TIME_DAY":mt5.ORDER_TIME_DAY,
            "ORDER_TIME_SPECIFIED":mt5.ORDER_TIME_SPECIFIED,
            "ORDER_TIME_SPECIFIED_DAY":mt5.ORDER_TIME_SPECIFIED_DAY
        }
    
    def __init__(self, path:str=None,
                       login:int=None,
                       password:str=None,
                       server:str=None,
                       timeout:int=None,
                       portable:bool=False):
        self.mt5 = mt5
        self.initialize(path, login, password, server, timeout, portable)

    def initialize(self, path:str=None,
                         login:int=None,
                         password:str=None,
                         server:str=None,
                         timeout:int=None,
                         portable:bool=False):
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",self.mt5.__author__)
        print("MetaTrader5 package version: ",self.mt5.__version__)
        isFail:bool = False
        if path and login and password and server and timeout and portable != None:
            # establish MetaTrader 5 connection to a specified trading account
            if not self.mt5.initialize(path=path,
                                       login=login,
                                       password=password,
                                       server=server,
                                       timeout=timeout,
                                       portable=portable):
                isFail = True
        elif path:
            if not self.mt5.initialize(path=path):
                isFail = True
        else:
            if not self.mt5.initialize():
                isFail = True
        if isFail:
            print("initialize() failed, error code =",self.mt5.last_error())
            quit()

    def shutdown(self):
        return self.mt5.shutdown()
    
    def accountInfo(self):
        return self.mt5.account_info()

    
    def terminalInfo(self):
        return self.mt5.terminal_info()

    def version(self):
        return self.mt5.version()
    
    def symbolsTotal(self):
        return self.mt5.symbols_total()
		
    
    def symbolsGet(self,group:str=None):
        if group:
            return self.mt5.symbols_get(group)
        else:
            return self.mt5.symbols_get()
		
    
    def symbolInfo(self,symbol:str):
        return self.mt5.symbol_info(symbol)
		
    
    def symbolInfoTick(self,symbol:str):
        return self.mt5.symbol_info_tick(symbol)
	
    
    def symbolSelect(self,symbol:str, enable:bool=True):
        return self.mt5.symbol_select(symbol, enable)	

    
    def copyRatesFrom(self,symbol:str, timeFrame:str,dateFrom:datetime,count:int):
        eTimeFrame = self._timeFrameDict.get(timeFrame,None)
        if eTimeFrame:
            return self.mt5.copy_rates_from(symbol,
                                            eTimeFrame,
                                            dateFrom,
                                            count) 	

    
    def copyRatesFromPos(self,symbol:str, timeFrame:str, startPos:int, count:int):
        eTimeFrame = self._timeFrameDict.get(timeFrame,None)
        if eTimeFrame:
            return self.mt5.copy_rates_from_pos(symbol, eTimeFrame, startPos, count)

    
    def copyRatesRange(self,symbol:str, timeFrame:str, dateFrom:datetime, dateTo:datetime):
        eTimeFrame = self._timeFrameDict.get(timeFrame,None)
        if eTimeFrame:
            return self.mt5.copy_rates_range(symbol, timeFrame, dateFrom, dateTo)

    
    def copyTicksFrom(self,symbol:str, dateFrom:datetime, count:int, flags:str):
        eFlags = self._eTickFlags.get(flags, None)
        if eFlags:
            return self.mt5.copy_ticks_from(symbol, dateFrom, count, eFlags)

    
    def copyTicksRange(self,symbol:str, dateFrom:datetime, dateTo:datetime, count:int, flags:str):
        eFlags = self._eTickFlags.get(flags, None)
        if eFlags:
            return self.mt5.copy_ticks_range(symbol, dateFrom, dateTo, eFlags)
    
    def ordersTotal(self):
        return self.mt5.orders_total()
		
    def ordersGet(self,symbol:str=None, group:str=None,ticket:int=None):
        if not (symbol or group or ticket):
            return self.mt5.orders_get()
        elif symbol:
            return self.mt5.orders_get(symbol=symbol)
        elif group:
            return self.mt5.orders_get(group=group)
        elif ticket:
            return self.mt5.orders_get(ticket=ticket)
        else:
            return
    
    def orderCalcMargin(self, action:str, symbol:str, volume:float, price:float):
        eAction = _eOrderType.get(action,None)
        if eAction:
            return self.mt5.order_calc_margin(eAction,
                                              symbol,
                                              volume,
                                              price)

    
    def orderCalcProfit(self, action:str, symbol:str, volume:float, price_open:float, price_close:float):
        eAction = _eOrderType.get(action,None)
        if eAction:
            return self.mt5.order_calc_profit(eAction,          
                                              symbol,
                                              volume,
                                              price_open,
                                              price_close)


    def _transformOrderRequest(self, orderRequest:dict):
        eAction = orderRequest.get("action",None)
        eType = orderRequest.get("type",None)
        eTypeTime = orderRequest.get("typeTime",None)
        eTypeFilling = orderRequest.get("typeFilling",None)
        request:dict = orderRequest
        if eAction and eType and eTypeTime and eTypeFilling:
            request["action"] = _eTradeRequestActions[eAction]
            request["type"] = _eOrderType[eType]
            request["type_time"] = _eOrderTypeTime[eType]
            request["type_filling"] = _eOrderTypeFilling[eTypeFilling]
            for removeKey in ["typeTime", "typeFilling"]: 
                if removeKey in request:
                    del request[removeKey]
            return request
        else:
            return
        
    
    def orderCheck(self, orderRequest:dict):
        request = self._transformOrderRequest(orderRequest)
        if request:
            return self.mt5.order_check(request)
    
    def orderSend(self, orderRequest:dict):
        request = self._transformOrderRequest(orderRequest)
        if request:
            return self.mt5.order_send(request)
    
    def positionsTotal(self):
        return self.mt5.positions_total()

    def positionsGet(self,symbol:str=None, group:str=None,ticket:int=None):
        if not (symbol or group or ticket):
            return self.mt5.positions_get()
        elif symbol:
            return self.mt5.positions_get(symbol=symbol)
        elif group:
            return self.mt5.positions_get(group=group)
        elif ticket:
            return self.mt5.positions_get(ticket=ticket)
        else:
            return

    
    def historyOrdersTotal(self,dateFrom:datetime,dateTo:datetime):
        return self.mt5.history_orders_total(dateFrom, dateTo)	
    
    def historyOrdersGet(self,dateFrom:datetime,dateTo:datetime,group:str):
        return self.mt5.history_orders_get(dateFrom, dateTo, group)
    
    def historyDealsTotal(self,dateFrom:datetime,dateTo:datetime):
        return self.mt5.history_deals_total(dateFrom, dateTo)
    
    def historyDealsGet(self,dateFrom:datetime,dateTo:datetime,group:str):
        return self.mt5.history_orders_get(dateFrom, dateTo, group)
