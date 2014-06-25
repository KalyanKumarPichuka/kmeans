#!/usr/bin/env Rscript
library(ggplot2)
x <- read.csv("in.tsv", header=FALSE, sep="\t")
names(x) <- c("size", "revenue", "class", "centroidsx", "centroidsy")

x$class <- factor(x$class)
x$classcentroids <- factor(x$centroidsx)
ggplot() +
    geom_point(data= x, aes(x=size, y=revenue, color=class), size=4) +
    geom_point(data= x, aes(x=centroidsx, y=centroidsy, color=class),shape=15, size=4) +
    ggtitle("GaussianNB classification of iris dataset.\nx's are training data, triangles are misclassified") +
    ggsave(file="plot1.png", width=10, height=7)
