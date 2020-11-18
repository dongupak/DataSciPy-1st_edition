# 단어에서 구두점을 제거하고 소문자로 만든다. 
def process(w): 
    output ="" 
    for ch in w: 
        if ch.isalpha() : 
            output += ch 
    return output.lower() 

words = set()  # 중복을 방지하기 위해 집합 자료형에 단어를 넣자
fname = input("입력 파일 이름: ") 
file = open(fname, "r")   # 파일을 연다
# 파일의 모든 줄에 대하여 반복한다. 
for line in file: 
      lineWords = line.split() 
      for word in lineWords: 
          words.add(process(word))   # 단어를 집합에 추가한다. 
 
print("사용된 단어의 개수 =", len(words)) 
print(words)