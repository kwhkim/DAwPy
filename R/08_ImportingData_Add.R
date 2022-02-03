# BOM 또는 UTF8-Signature 확인 방법
f <- file("서울시 한강공원 이용객 현황 (2009_2013년).csv", "rb")
marks <- readBin(f, "raw", n=10)

# 출처: https://en.wikipedia.org/wiki/Byte_order_mark
BOM_UTF8 <- as.raw(c(0xef, 0xbb, 0xbf))
BOM_UTF16BE <- as.raw(c(0xfe, 0xff))
BOM_UTF16LE <- as.raw(c(0xff, 0xfe))
BOM_UTF32BE <- as.raw(c(0x00, 0x00, 0xfe, 0xff))
BOM_UTF32LE <- as.raw(c(0xff, 0xfe, 0x00, 0x00))
BOM_UTF7 <- as.raw(c(0x2b, 0x2f, 0x76))
BOM_UTF1 <- as.raw(c(0xf7, 0x64, 0x4c))
BOM_UTF_EBCDIC <- as.raw(c(0xdd, 0x73, 0x66, 0x73))
BOM_SCSU <- as.raw(c(0x0e, 0xfe, 0xff))
BOM_BOCU1 <- as.raw(c(0xfb, 0xee, 0x28))
BOM_GB18030 <- as.raw(c(0x84, 0x31, 0x95, 0x33))
BOMs = list("UTF8"=BOM_UTF8, 
            "UTF16BE"=BOM_UTF16BE, "UTF16LE"=BOM_UTF16LE, 
            "UTF32BE"=BOM_UTF32BE, "UTF32LE"=BOM_UTF32LE,
            "UTF7"=BOM_UTF7, "UTF1"=BOM_UTF1, 
            "UTF-EBCDIC"=BOM_UTF_EBCDIC, 
            "SCSU"=BOM_SCSU, 
            "BOCU-1"=BOM_BOCU1, 
            "GB-18030"=BOM_GB18030)

check_marks = function(BOM) {
    if (all(marks[1:length(BOM)] == BOM)) return(TRUE) else return(FALSE)
}

names(BOMs)[sapply(BOMs, check_marks)]

# ====
# 함수로 만들기
# checkBOM(filename)

checkBOM = function(filename) {
    marks <- readBin(filename, "raw", n=4)

    BOM_UTF8 <- as.raw(c(0xef, 0xbb, 0xbf))
    BOM_UTF16BE <- as.raw(c(0xfe, 0xff))
    BOM_UTF16LE <- as.raw(c(0xff, 0xfe))
    BOM_UTF32BE <- as.raw(c(0x00, 0x00, 0xfe, 0xff))
    BOM_UTF32LE <- as.raw(c(0xff, 0xfe, 0x00, 0x00))
    BOM_UTF7 <- as.raw(c(0x2b, 0x2f, 0x76))
    BOM_UTF1 <- as.raw(c(0xf7, 0x64, 0x4c))
    BOM_UTF_EBCDIC <- as.raw(c(0xdd, 0x73, 0x66, 0x73))
    BOM_SCSU <- as.raw(c(0x0e, 0xfe, 0xff))
    BOM_BOCU1 <- as.raw(c(0xfb, 0xee, 0x28))
    BOM_GB18030 <- as.raw(c(0x84, 0x31, 0x95, 0x33))
    BOMs = list("UTF8"=BOM_UTF8, 
                "UTF16BE"=BOM_UTF16BE, "UTF16LE"=BOM_UTF16LE, 
                "UTF32BE"=BOM_UTF32BE, "UTF32LE"=BOM_UTF32LE,
                "UTF7"=BOM_UTF7, "UTF1"=BOM_UTF1, 
                "UTF-EBCDIC"=BOM_UTF_EBCDIC, 
                "SCSU"=BOM_SCSU, 
                "BOCU-1"=BOM_BOCU1, 
                "GB-18030"=BOM_GB18030)

    check_marks = function(BOM) {
        if (all(marks[1:length(BOM)] == BOM)) return(TRUE) else return(FALSE)
    }

    res = names(BOMs)[sapply(BOMs, check_marks)]
    if (length(res)>0) {
        con = file(filename, "rb")
        readBin(con, "raw", n = length(BOMs[[res]]))
        return(list(BOM=res, con=con))
    } else {
        return(list(BOM="", con=file(filename), "rb"))
    }
    
}

filename = "서울시 한강공원 이용객 현황 (2009_2013년).csv"
#filename = "08_ImportingData_Add.R"
res = checkBOM(filename)
res$BOM
if (res$BOM != "") {
  fsize = file.size(filename)
  x <- readBin(res$con, what = 'raw', n=fsize + 1)
  y <- rawToChar(x)
  Encoding(y) <- res$BOM
  # 이렇게 하면 res$BOM이 UTF-8 일 떄만 성공
  # 하지만 다른 인코딩이면 rawToChar(x)에서 에러가 날 확률이 높음
  # 에러가 나지 않는다면
  # iconv(y, res$BOM, "")와 같이 default encoding으로 인코딩을 변환하거나
  # iconv(y, res$BOM, "UTF-8")로 변환하고, Encoding() <- "UTF-8"로 마무리해야 할 듯
  cat(y)
}


read_csv(filename, locale(encoding = 'UTF-8-BOM')) # Error: Unknown encoding UTF-8-BOM
read_csv(res$con, locale(encoding = 'UTF-8'))
read_csv(filename, )


## 참고자료

* https://stackoverflow.com/questions/39593637/dealing-with-byte-order-mark-bom-in-r
* https://118k.tistory.com/863
