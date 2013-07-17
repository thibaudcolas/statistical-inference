# Statistical inference applied on EPI, BF and BDI scores

## Loading the dataset

To load the dataset into R :

```r
  data <- read.csv(file="epi-bf-bdi-data.csv",head=T, sep="\t")
```

- `read.csv` Loads the file content into R
- `file` : Path to the file
- `head = T` : Tells R that there is a headline
- `sep = "\t"` : Tells R that values are separated by tabs

We can assert that the file was successfully read with `names` :

```r
  > names(data)
  [1] "epiE"     "epiS"     "epiImp"   "epilie"   "epiNeur"  "bfagree"  "bfcon"
  [8] "bfext"    "bfneur"   "bfopen"   "bdi"      "traitanx" "stateanx" "sex"
  [15] "age"
```

We then use `attach` to facilitate access to the vectors inside the dataframe.

```r
  > attach(data)
```

To see how big the dataset is, we use `dim` :

```r
  > dim(data)
  [1] 231  15
```

We thus have 231 results for fifteen variables.
