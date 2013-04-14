WebPageIsometer
===============

Proposal for Information Retrieval(CSCE-670) final project
Project Name: Web Page Isometer
Team Members: Pradipta Kumar Bose, Sanjeev Kumar Singh, Santanu Saha

What is exactly the function of your tool? That is, what will it do?
Finding similarity between web pages on the basis of their contents, structures and visual features.
Why would we need such a tool and who would you expect to use it and benefit from it?
If a web-designer designs a web page and wants to assure that the designed web page follows the latest
trend in its category and it’s not erratic in content, structure and appearance, then this tool can be
handy.
Thus, we aim to provide a new web presence with some feedback regarding their web page design
vis-a-vis their peers in the same domain.

Does this kind of tools already exist? If similar tools exist, how is your tool different from them?
Would people care about the difference? How hard is it to build such a tool? What is the
challenge?
There are some existing tools which serves the same purpose. However, we are yet to find a tool that
considers all the three aspects viz. content, structure and appearance to compute similarity between web
pages. Consideration of all the three implicit attributes of a web page and their quantification will stand
out in terms of usability for different applications of Information Retrieval.
Coming up with a new algorithm which actually considers all the three essential aspects of a given web
page is a challenge in itself. Also, implementing algorithms for quantifying the structural and visual
similarity between web pages will be something which we haven’t discussed in our course

How do you plan to build it? You should mention the data you will use and the core algorithm
that you will implement.
We will be implementing a few algorithms in order to quantify the three implicit features of a web page
viz. content, structure and appearance and then after pondering over different tools and techniques we
will try to come up with an algorithm which can quantify the similarity of one web page to another
keeping all the three aspects into consideration.
On the basis of our research till now, we have thought of implementing ‘Edit Distance’ or ‘Tag
Similarity’ for finding Structural Similarity and some variation of Cosine Similarity for quantifying
Content Similarity.
We are yet to come up with something concrete in order to quantify Visual Similarity betweentwo web
pages. We have gone through some of the existing libraries - Python Imaging Library, OpenCV
and the like, and are making steady progress in this area.
However, the bigger challenge will be to find a way to merge all of these and come up with a
completely new algorithm keeping logical justification in place.
We will be considering the web pages from the Alexa Top 100 (http://www.alexa.com) as our data set.
We might just consider a few categories like- sports or arts in order to analyze our implementation.

What existing resources can you use?
In order to understand and analyze the implicit and explicit features of web page, we will be
considering sample pages available on the web. Also, we will be considering web pages from Alexa
Top 100 for analyzing and improving our implementation. Since, our work has more inclination
towards research rather than core development, so w will go through the related literature available on
web in the form of papers, articles or journals.

How will you demonstrate the usefulness of your tool?
As a new page is introduced, our tool should be able to give a measure of similarity for different
existing web pages with respect to the introduced page. This would be useful especially to web
designers , who would then have some quantifiable benchmarks to work towards.
