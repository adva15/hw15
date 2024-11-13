#1
import random

list_50=[random.randint(1,100) for i in range(50)]
print(list_50)
#a
list_50_filter=list(filter(lambda num:num >50,list_50))
print("filter=",list_50_filter)
#b
list_50_filter=list(filter(lambda num:num % 7==0,list_50))
print(" %7 =",list_50_filter)
#c
list_50_filter=list(filter(lambda num:10<= num <=99,list_50))
print(" 10<=99 =",list_50_filter)
#d
list_50_filter=list(filter(lambda num:num % 10==num //10 ,list_50))
print(" ahadot=asarot =",list_50_filter)
#e לחזור!!
# list_50_filter=list(filter(lambda num: sum(num)==9 ,list_50))
# print(" sum9=",list_50_filter)
#f
avg_list=sum(list_50)/len(list_50)
list_greater_avg=list(filter(lambda num: num > avg_list ,list_50))
print("greater avg =",list_greater_avg)
#g
max_half=max(list_50)
greater_max_half=list(filter(lambda num: num > max_half / 2 ,list_50))
print("greater maximum half =",greater_max_half)

#2.
list_play=["Grand Theft Auto V","Fortnite","The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
#a
list_play_8=list(filter(lambda l: len(l) >8 ,list_play))
print("list-letters 8=",list_play_8)
#b
list_play_8=list(filter(lambda word: word.startswith("F") ,list_play))
print("list-letter f=",list_play_8)
#c
list_play_8=list(filter(lambda word: len(word) <=2 ,list_play))
print("list-word 2=",list_play_8)
#d
list_play_v=list(filter(lambda word:'v' in word.lower(),list_play))
print("list-letter v=",list_play_v)

#3
list_20=[random.randint(-50,50) for _ in range(20)]
print(list_20)
#a
list_20_Power=list(map(lambda num:num **3 ,list_20))
print("Power 3=",list_20_Power)
#b
list_20_ahadot=list(map(lambda num:num %10 ,list_20))
print("ahadot=",list_20_ahadot)
#c
list_20_Fahrenheit=list(map(lambda num:num *9/5+32 ,list_20))
print("Fahrenheit=",list_20_Fahrenheit)
#d


#4
list_fruits=["Mango","Orange","Banana","Apple","Strawberry","Pineapple","Grapes","Watermelon"]
#a
swap_letters=list(map(lambda word:word [::-1]  ,list_fruits))
print("swap letters=",swap_letters)
#b
list_fruits_First_letter=list(map(lambda word:word[0] ,list_fruits))
print("First letter=",list_fruits_First_letter)
#c
list_fruits_big_letter=list(map(lambda word: word.upper(),list_fruits))
print("big letters=",list_fruits_big_letter)
#d
list_fruits_Middle_letter=list(map(lambda word: word[len(word) // 2],list_fruits))
print("Middle letter=",list_fruits_Middle_letter)
#e-bonus


#5.
#השימוש בגלובל הוא כאשר רוצים לשנות ערך, אנו מחליטים מה יהיה בערך הגלובלי שלו בפונקציה.
#החסרונות של השימוש בו זה שהוא פוגע בקריאות ובנראות של הקוד ובנוסף הוא תלוי בהגדרות ובכך מקשה על שימוש חוזר בפונקציה של הקוד

# x: int = 1
# def foo():
#  print(x)
# x = 4
# foo()

#זה שגוי כיוון ש-X לא במיקום שהוא אמור להיות בו