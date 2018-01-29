# Copyright 2013-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from __future__ import absolute_import, print_function

import os
import glob
import tempfile
import shutil
from jt.jpype import *

LUCENE_HOME = os.environ.get("LUCENE_HOME")
if not LUCENE_HOME:
    raise EnvironmentError("Please set LUCENE_HOME environment variable "
                           "to Lucene (version 4.10.0 or above) directory")

lucene_jars = [LUCENE_HOME + "/core/*.jar",
               LUCENE_HOME + "/analysis/common/*.jar",
               LUCENE_HOME + "/queryparser/*.jar"]

jvm_path     = getDefaultJVMPath()
jars_paths   = sum((glob.glob(jar_path) for jar_path in lucene_jars), [])
temp_dirname = tempfile.mkdtemp()

print("Running using JVM:", jvm_path)
print()

startJVM(jvm_path, "-ea", '-Djava.class.path={}'.format(os.pathsep.join(jars_paths)))

FSDirectory                = JClass("org.apache.lucene.store.FSDirectory")
IndexWriterConfig          = JClass("org.apache.lucene.index.IndexWriterConfig")
IndexWriter                = JClass("org.apache.lucene.index.IndexWriter")
IndexReader                = JClass("org.apache.lucene.index.IndexReader")
IndexSearcher              = JClass("org.apache.lucene.search.IndexSearcher")
QueryParser                = JClass("org.apache.lucene.queryparser.classic.QueryParser")
StandardAnalyzer           = JClass("org.apache.lucene.analysis.standard.StandardAnalyzer")
SimpleAnalyzer             = JClass("org.apache.lucene.analysis.core.SimpleAnalyzer")
Document                   = JClass("org.apache.lucene.document.Document")
Field                      = JClass("org.apache.lucene.document.Field")
StringField                = JClass("org.apache.lucene.document.StringField")
TextField                  = JClass("org.apache.lucene.document.TextField")
IntField                   = JClass("org.apache.lucene.document.IntField")
FloatField                 = JClass("org.apache.lucene.document.FloatField")
StoredField                = JClass("org.apache.lucene.document.StoredField")
Version                    = JClass("org.apache.lucene.util.Version")
IndexWriterConfig_OpenMode = JClass("org.apache.lucene.index.IndexWriterConfig$OpenMode")
Field_Store                = JClass("org.apache.lucene.document.Field$Store")

version   = Version.LUCENE_CURRENT
analyzer  = StandardAnalyzer(version)
directory = FSDirectory.open(java.io.File(temp_dirname))

iwconfig = IndexWriterConfig(version, analyzer)
iwconfig.setOpenMode(IndexWriterConfig_OpenMode.CREATE)
iwriter  = IndexWriter(directory, iwconfig)
iwriter.commit()

doc = Document()
doc.add(TextField("title",    "Solaris",         Field_Store.YES))
doc.add(TextField("author",   "Stanislav Lem",   Field_Store.YES))
doc.add(TextField("category", "science fiction", Field_Store.YES))
doc.add(IntField("pages",     326,               Field_Store.YES))
doc.add(FloatField("price",   23.40,             Field_Store.YES))
iwriter.addDocument(doc)
iwriter.commit()

doc = Document()
doc.add(TextField("title",    "Cyberiada",       Field_Store.YES))
doc.add(TextField("author",   "Stanislav Lem",   Field_Store.YES))
doc.add(TextField("category", "science fiction", Field_Store.YES))
doc.add(IntField("pages",     141,               Field_Store.YES))
doc.add(FloatField("price",   18.60,             Field_Store.YES))
iwriter.addDocument(doc)
iwriter.commit()

doc = Document()
doc.add(TextField("title",    "Golem XIV",       Field_Store.YES))
doc.add(TextField("author",   "Stanislav Lem",   Field_Store.YES))
doc.add(TextField("category", "science fiction", Field_Store.YES))
doc.add(IntField("pages",     78,                Field_Store.YES))
doc.add(FloatField("price",   53.20,             Field_Store.YES))
iwriter.addDocument(doc)
iwriter.commit()

iwriter.close()

ireader  = IndexReader.open(directory)
searcher = IndexSearcher(ireader)
qparser  = QueryParser(version, None, analyzer)
querystr = "title:{} OR author:{}".format('"Solaris"', '"Stanislav Lem"')
query    = qparser.parse(querystr)
hits     = searcher.search(query, 50)

print("Query:", query)
print()
for i, item in enumerate(hits.scoreDocs):
    doc = searcher.doc(item.doc)
    print("{:2}. '{}'\t{}\t{:3} pages".format(
          i + 1, doc.get("title"), doc.get("author"), doc.get("pages")))
    #print(str(doc))

shutil.rmtree(temp_dirname, ignore_errors=True)
shutdownJVM()
