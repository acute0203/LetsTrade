import abc
from contextlib import AbstractContextManager

class PlatformInterface(AbstractContextManager):
 
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented
 
    @abc.abstractmethod
    def accountInfo(self):
        return NotImplemented
		
    @abc.abstractmethod
    def terminalInfo(self):
        return NotImplemented

    @abc.abstractmethod
    def version(self):
        return NotImplemented
    
    @abc.abstractmethod
    def symbolsTotal(self):
        return NotImplemented
		
    @abc.abstractmethod
    def symbolsGet(self):
        return NotImplemented
		
    @abc.abstractmethod
    def symbolInfo(self):
        return NotImplemented
		
    @abc.abstractmethod
    def symbolInfoTick(self):
        return NotImplemented
	
    @abc.abstractmethod
    def symbolSelect(self):
        return NotImplemented	

    @abc.abstractmethod
    def copyRatesFrom(self):
        return NotImplemented	

    @abc.abstractmethod
    def copyRatesFromPos(self):
        return NotImplemented

    @abc.abstractmethod
    def copyRatesRange(self):
        return NotImplemented

    @abc.abstractmethod
    def copyTicksFrom(self):
        return NotImplemented

    @abc.abstractmethod
    def copyTicksRange(self):
        return NotImplemented

    @abc.abstractmethod
    def ordersTotal(self):
        return NotImplemented
		
    @abc.abstractmethod
    def ordersGet(self):
        return NotImplemented	

    @abc.abstractmethod
    def orderCalcMargin(self):
        return NotImplemented	

    @abc.abstractmethod
    def orderCalcProfit(self):
        return NotImplemented	
		
    @abc.abstractmethod
    def orderCalcProfit(self):
        return NotImplemented	

    @abc.abstractmethod
    def orderCheck(self):
        return NotImplemented

    @abc.abstractmethod
    def orderSend(self):
        return NotImplemented

    @abc.abstractmethod
    def positionsTotal(self):
        return NotImplemented

    @abc.abstractmethod
    def positionsGet(self):
        return NotImplemented

    @abc.abstractmethod
    def historyOrdersTotal(self):
        return NotImplemented
		
    @abc.abstractmethod
    def historyOrdersGet(self):
        return NotImplemented
		
    @abc.abstractmethod
    def historyOrdersGet(self):
        return NotImplemented

    @abc.abstractmethod
    def historyDealsTotal(self):
        return NotImplemented
		
    @abc.abstractmethod
    def historyDealsGet(self):
        return NotImplemented

    @abc.abstractmethod
    def shutdown(self):
        return NotImplemented
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()
        print(self.__class__.__name__,"class shutdown....")
