wave <- read.table("~/BigDataLite1.2/shared/linear_regression_bootcamp/wave.dat", quote="\"")
multivariate <- read.table("~/BigDataLite1.2/shared/linear_regression_bootcamp/multivariate.dat", quote="\"")
white_noise_shocks <- read.table("~/BigDataLite1.2/shared/linear_regression_bootcamp/white_noise_shocks.dat", quote="\"")
wns <- white_noise_shocks[0:2000,]

#basic multivariates
par(mfrow=c(1,3))
scatterplot3d(mv$x1, mv$y,highlight.3d=TRUE,
col.axis="blue", col.grid="lightblue")
scatterplot3d(mv$x2, mv$y,highlight.3d=TRUE,
col.axis="blue", col.grid="lightblue")
scatterplot3d(mv$x3, mv$y,highlight.3d=TRUE,
col.axis="blue", col.grid="lightblue")
plot(multivariate$x1, multivariate$y)
plot(multivariate$x2, multivariate$y)
plot(multivariate$x3, multivariate$y)
ks.test(multivariate[,c("x1","x2","x3")], multivariate$y)
m <- lm(y ~ x1*x2*x3, data=multivariate)
m2 <- lm(y ~ x1*x2 + I(x1*x2), data=multivariate)

#time series decompositiontrend <- data.frame(decomp.wave$trend, wave$V1)
twave <- ts(wave$V2, frequency=200)
plot(twave)
decomp.wave <- decompose(twave)
plot(decomp.wave)
trend <- data.frame(decomp.wave$trend, wave$V1)
names(trend) <- c("y","x")
tmodel <- lm(y ~ x, data=trend,na.omit=TRUE)
plot(decomp.wave$seasonal)
plot(ma(decomp.wave$seasonal,100))
#bonus: the 'seasonal' component is just a sine wave
nmodel <- nls(x ~ A*sin(x), data=seas, start=list(A=1))
summary(nmodel)


# finding control limits on an MA model
aa <- auto.arima(as.ts(wns$V2,frequency=1000))
summary(aa)
applied.model <- filter(wns$V2, c(-0.43,-.12,-0.35), "recursive")
plot(wns$V1,applied.model)
mean(applied.model)
mean(applied.model)+3*sd(applied.model)
mean(applied.model)-3*sd(applied.model)


