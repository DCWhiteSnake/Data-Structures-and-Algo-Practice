class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero.
        
        customer    the name of the  customer(e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier(e.g., '5391 0375 9387 5309')
        limit       credit limit(measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
        
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
        
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
        
    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account
        
    def get_limit(self):
        """Return current card limit."""
        return self._limit
        
    def get_balance(self):
        """Retutn current balance."""
        return self._balance

    def _set_balance(self, balance):
        self._balance += balance


    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Raise a ValueError if the user doesn't submit a float as price.
        Return True if charge was processsed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise ValueError("Price must have a floating point value")
        else:
            if price + self._balance > self._limit:    #if charge would exceed limit,
                return False                           # cannot accept charge
            else: 
                self._balance += price
                return True
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if amount < 0:
            raise ValueError("Cannot enter a negative amount")
        if not isinstance(amount,(int, float)):
            raise TypeError("Please enter a valid amount")
        else:
            self._balance -= amount
            
        

class PredatoryCreditCard(CreditCard):
    """ An extension to CreditCard that compounds interest and fees. """

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """

        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        """
        assess_penalty = 0
        success = super().charge(price) # call inherited method
        if not success:
            assess_penalty -= 5
            super()._set_balance( - price + assess_penalty) # assess penalty
        return success # caller expects return value

    def process_month(self):
       """Assess monthly interest on outstanding balance."""
       if self.get_balance() > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self. apr, 1/12)
            self.set_balance = monthly_factor



if __name__ == '__main__':
    simi_creditcard = PredatoryCreditCard('Simi','Zenith','1224141',1000,0.085)
    print(simi_creditcard.get_balance())
    simi_creditcard.charge(1500)
    print(simi_creditcard.get_balance())  # output 1505
