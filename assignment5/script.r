library (caret)
library (ggplot2)
library (rpart)
library (randomForest)
library (e1071)

da = read.csv ("seaflow_21min.csv")
names (da)
summary (da)

ind = createDataPartition (seq(1,dim(da)[1]), times=2, p=0.5, list=TRUE)
train=da[ind$Resample1,]
test=da[ind$Resample2,]

summary(train)
summary(test)

ggplot(da) + geom_point(aes(x=da$pe, y=da$chl_small, color=da$pop, size=2))

fol <- formula (pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)

# Decision tree
model <- rpart (fol, method="class", data=train)
print(model)

prediction <- predict (model, newdata=test, type="class")
prob <- sum (prediction == test$pop)/nrow(test)
prob

# Random forest
model2 <- randomForest (fol, data=train, nodesize=10)
print(model2)

prediction2 <- predict (model2, newdata=test, type="class")
prob <- sum (prediction2 == test$pop)/nrow(test)
prob

importance (model2)

# SVM
model3 <- svm (fol, data=train)
print(model3)

prediction3 <- predict (model3, newdata=test, type="class")
prob <- sum (prediction3 == test$pop)/nrow(test)
prob

table (pred=prediction,  true=test$pop)
table (pred=prediction2, true=test$pop)
table (pred=prediction3, true=test$pop)

not = da[da$file_id!=208,]
ind2 <- createDataPartition (seq(1,dim(not)[1]), times=2, p=0.5, list=TRUE)
train <- not[ind2$Resample1,]
test  <- not[ind2$Resample2,]

# Decision tree (after removing corrupted data)
model <- rpart (fol, method="class", data=train)
print(model)

prediction <- predict (model, newdata=test, type="class")
prob <- sum (prediction == test$pop)/nrow(test)
prob

# Random forest
model2 <- randomForest (fol, data=train, nodesize=10)
print(model2)

prediction2 <- predict (model2, newdata=test, type="class")
prob <- sum (prediction2 == test$pop)/nrow(test)
prob

importance (model2)

# SVM
model3 <- svm (fol, data=train)
print(model3)

prediction3 <- predict (model3, newdata=test, type="class")
prob <- sum (prediction3 == test$pop)/nrow(test)
prob

