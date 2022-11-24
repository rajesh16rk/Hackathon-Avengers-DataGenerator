from IPython.core.debugger import set_trace
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker

def main():
    
    fake = Faker()
    
    def faker_timeseries_row(num = 1, seed = None):
    
        fake.seed_instance(seed)
        
        time_gen = fake.time_series(start_date=f"-{num}d", end_date="now", precision = 3600)
        
        output = [
            {
                
                "name": fake.last_name(),
                "email": fake.free_email(),
                "datetime": next(time_gen),
                "ssn": fake.ssn(),
                "creditcard": fake.credit_card_number(),
                "pricetag": fake.pricetag(),
                "country": fake.country()
                
            }
            
            for x in range(num)
        ]
        
        return output
    
    df = pd.DataFrame(faker_timeseries_row(30, seed=0))

    print(df.to_string())
    
    
if __name__ == '__main__':
    
    main()
    
    