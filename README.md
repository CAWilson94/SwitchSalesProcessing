# SwitchSalesProcessing
Sales Messages Processing 

*Assumptions:* 

Sales come in in batches, e.g. with a bob job or something similar (perhaps once every day). 
The message format has been agreed on before hand and will not change -
e.g. Message type 1 is of format <product> at value
Message type 2 is of format <number> of <product> at <value> each
Message type 3 is of format <operation> <adjustment_value> <product>
  
*To Run*: 
Go to message_processing_app.py and run from the main here. 

## Method
I wrote down some products represented by nintendo switch games and assigned these prices. There are perhaps 
ten in total different products with prices. 

## Data Generation 

To generate input data I created a script called "data_generator.py" which has three classes - one for each message type. 
The base Data generator is inerited by the other two as it shares some functionality. 

I took in file input from written up products with their values and assigned each a random message number which determined which data
generator would then generate data for each row in the file. 

The output was a large csv / pandas df with columns such as total value, value, operation etc all the data required. 
I then formatted this out to a text file to use as input to the actual message processing application. 

The application has a few parts - a sales class, a message processing app (as main demo runner), a report class and a message processing class. 

## Sales Class 

The sales class is used to store each sale object, and any adjustments that are applied to it (in the form of named tuple). 
The adjustments are stored in a list and then they are all applied in bulk when required so that sale values can be aggregated accordingly. 
There are also to dict methods for applied adjustments and each sale object itself for easier manipulation when it comes to logging. 

## Message Processing

For message processing, each message was checked for type 1, 2 or 3 (adjustment) and then parsed in the appropriate way. 
Adjustments were applied on recieving adjustment messages (message 3). 
Also, the requirements specify that the logger should output a basic report every 10 *messages* which is easy to confuse for every 10 sales.
So, there is a count for incoming messages to check this. 
To aid the message type checkig, there is a list of unused words in the messages such as "of", "at" and "each".`

## Report

The report creation mostly consists of making use of pandas df module in which data can easily be split up and have logic applied 
per column, group etc. On instantiation, the report takes in a sales list and then converts this to a pandas df using the to dict method of each sale 
and thereafter using from_records to turn a list of sales dicts to a pandas df which can be used easily for all reporting and calculations. 

## Testing: 

Used basic python unittest library and mocking
