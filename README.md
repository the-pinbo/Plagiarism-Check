# Doc2vec

***Finding Doc2vec***

Initially I was planning on implementing a **Word2vec** model as I thought that word embeddings would perform better than tf-idf because they would generate the vectors for words based on the context of the text 
but I realised that it would be difficult to compare documents as they would be a matrix of vectors of different sizes.

As taking the cosine similarity of those matrices would not be possible because of different dimensions of the matrices (which is because of different number of words in each doucment). And averaging out didn't seem like a viable option since it dilutes the vector embeddings leading to loss of data.

### Problems with word2vec 
 - gives one vector per word, so gives set of vectors for a document, so hard to take cosine similarty			
available methods 
### Possible solutions
- take mean and proceed.			
- [using the paragraph vector](https://cs.stanford.edu/~quocle/paragraph_vector.pdf)
- [some say it is extrmely difficult(2 ans in the given link)](https://stackoverflow.com/questions/15173225/calculate-cosine-similarity-given-2-sentence-strings/15173821#15173821)		

<br></br>

> ## Doc2vec

This was better model to implement as this keeps track of the paragraph using a para-id which is included within the vector embedding. The links to the implementation guide and research paper are given below.


- [Sentence / Document Similarity](https://stackoverflow.com/questions/22129943/how-to-calculate-the-sentence-similarity-using-word2vec-model-of-gensim-with-pyt)		
- [Refecence for implementation](https://towardsdatascience.com/calculating-document-similarities-using-bert-and-other-models-b2c1a29c9630)
- [Paragraph vector-Research paper](https://cs.stanford.edu/~quocle/paragraph_vector.pdf)



>Current problem

Trying to understand the reason behind negative similarty results. We know it is due to negative value document vecotr generation by the model. trying to understand its meaning and possible function to map the range of results fro -1 to 1 to 0 to 1.

<br></br>

# Possible future endeavours

> ## Universal sentence Encoder
- Why use universal sentence encoder(https://stackoverflow.com/questions/8897593/how-to-compute-the-similarity-between-two-text-documents)
- [Research Paper](https://arxiv.org/pdf/1803.11175.pdf)
				

> ## Other methods
- [StackOverflow reference](https://stackoverflow.com/questions/22129943/how-to-calculate-the-sentence-similarity-using-word2vec-model-of-gensim-with-pyt)
> ## All the similarity methods
- [medium refernce](https://medium.com/analytics-vidhya/best-nlp-algorithms-to-get-document-similarity-a5559244b23b)
