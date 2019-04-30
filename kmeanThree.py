from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import argparse, csv

#creating parser object -DC
parser = argparse.ArgumentParser(description='kmean, iteration, file')

#passing # of clusters to kval -DC
parser.add_argument('-k', type=int, dest="kvalue")

#passing # of iterations to ival -DC
parser.add_argument('-it', type=int, dest="ivalue")

#passing line separated file to testfile -DC
parser.add_argument('-test', action="store", dest="testfile", help="input file CSV, format: (time), can interface, msgid, data")

#passing line separated file to trainfile -DC
parser.add_argument('-train', action="store", dest="trainfile", help="input file CSV, format: (time), can interface, msgid, data")

#creating parse_arg() object to read argument results -DC
results = parser.parse_args()

# # of clusters -DC
kval = results.kvalue
# # of iterations -DC
ival = results.ivalue

# reading testfile into reader -DC
test = open(results.testfile, 'r')
readertest = csv.reader(test, delimiter='\n')

# reading trainfile into reader -DC
train = open(results.trainfile, 'r')
readertrain = csv.reader(train, delimiter='\n')

#list element to store data -DC
docTest = []

#list element to store data -DC
docTrain = []

#passing test data, line by line, into the list of elements -DC
for line in readertest:
	sent = line[0]
	docTest.append(sent)
	#print (sent.strip())

#passing training data, line by line, into the list of elements -DC
for line in readertrain:
	sent = line[0]
	docTrain.append(sent)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(docTrain)
true_k = kval
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=ival, n_init=1)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
   print("Cluster %d:" % i),
   for ind in order_centroids[i, :10]:
       print(' %s' % terms[ind]),
   print
print("\n")
print("Prediction")



Y = vectorizer.transform(docTest)
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(docTest)
prediction = model.predict(Y)
print(prediction)
