# Creates a variable named a, and assigns it the value2 .
a<-2
# Create a variable named b with value 5
b<-5
# Compute a+b and store the result in a variable named c
c<-a+b
print(c)


# Replace the value of a by 3
a<-3
print(a)
# Print out the value of c 
# Is-it still true that c=a+b? Why?
c ==a+b
print(c)
# Interpretation:==tests whether two variables have 
# the same content. 
# The result is a logical value (TRUE orFALSE).

a<-27
c<-a+b
print(c)
c == a+b


### Vectors of values ###
threeNumbers<- c(27,12,3000)
print(threeNumbers)

### Series of numbers ### 
x<- 0:30
print(x)
print(0:3)
print(58:136)

### Computing with series ###
x<-1:10
print(x)
y<-x*x
print(y)

### Sequences of numbers ###
seq(from=-1, to=1, by=0.1)

### Variables can also contain text ###
whoami = c("Denis", "Simeon")
print(whoami)

### String concatenation ###  

# concatenate string-containing variables
firstName <-paste(collapse = "-", whoami)
print(firstName)

# concatenate tw vectors 
lastName <- "Poisson"
print(paste(sep = " ", firstName, lastName))

# Concatenate 2 vectors with 3 values each
firstNames <- c("George", "Alfred", "Fred")
lastNames <- c("Sand", "Musset", "Chopin")
fullNames <- paste(sep = " ", firstNames, lastNames)
print(fullNames)

# Concatenate all the values of a given vector
fullNames2 <- paste(collapse = ", ", firstNames, lastNames)
print(fullNames2)


### Graphical functions ###

# scatter plot # 
x <- seq(from = -10, to = 10, by = 0.1)
y<- x*x
plot(x,y)

# curve (line plot) #
plot(x,y, 
     type="l", 
     main = "title", 
     xlab="test",
     col="blue", 
     lwd = 3,
     las = 3
     )
grid(nx = 5, 
     ny = 5, 
     col = "gray", 
     lty = "dotted",
     lwd = 1)
abline(h=0, col = "red")
abline(v=0, col = "green")

### Probabilities distribution ### 

# pmf : We can use the pmf to calculate the 
# probability of a particular outcome of the 
# experiment. For example, what is the 
# probability of seeing 6 successes? 
# We can use the dbinom function.
n <- 13
p <- 0.7
x <- 0:n
dbinom(6, size = n, prob = p)

# this is the entire pmf 
plot(x, 
     dbinom(x, size = n, prob = p),
     type = "l",
     main = "Probability mass function 
     for Bin(13,0.7)"
     )

# CDF : If we want to calculate the probability 
# of observing an outcome less than or equal 
# to a particular value, we can use the 
# cumulative distribution function. 
# For example, what is the probability of 
# observing 9 or fewer successes?

pbinom(9, size = n, prob = p)
plot(x, 
     pbinom(x, size = n, prob = p), 
     type="s", 
     main = "Cumulative distribution function 
     for Bin(13,0.7)"
     )

# EXEMPLE #


