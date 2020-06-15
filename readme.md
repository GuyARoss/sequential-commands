## Sequential Commands

#### Problem Statement:
Detecting sequential commands can be difficult, expecially when we apply some compute contraints. When I talk to something I really dont want to wait more than a second or two for a response.

__E.g.__
When a system is provided the following statement
"*Add 52 to the low of San Francisco*" intuitively as humans, we know at a high level we really need to complete 2 tasks here, first we need to find the low of san francisco and second add 52 to that value.

#### Approach(s):
Ya.. just trying a couple ideas out here.. 

##### Ap. 0
At a high level, in our dataset, we have a property for a delimiting phrase that represents where each statement should be split. e.g in the statement "*could you add twelve to the max temperature in London*" our delimiting property would be "*to the*". Given this, it is really just a matter of learning the boundaries from our dataset and detecting any oscillation that may exist when comparing our input to said boundaries.

__cons__:
- our dataset needs to have a delimiter present.
- not a whole lot of context. (
    a good approach to this problem might be including what tags are before and after each of the delimiters. Then checking the probability during prediction time. trie?
)
