{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Chapter 1. \n",
    "# 알고리즘 기초\n",
    "# Unit 1. 알고리즘과 플로우 차트"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 문자열과 숫자 입력받기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름을 입력하세요.: 이성욱\n",
      "안녕하세요? 이성욱님.\n"
     ]
    }
   ],
   "source": [
    "name = input('이름을 입력하세요.: ')\n",
    "print(f'안녕하세요? {name}님.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정사각형의 한 변의 길이를 입력하세요.: 5\n",
      "정사각형의 넓이는 25입니다.\n"
     ]
    }
   ],
   "source": [
    "length = input('정사각형의 한 변의 길이를 입력하세요.: ')\n",
    "print(f'정사각형의 넓이는 {int(length)**2}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 세 정수를 입력받아 최댓값 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "세 정수의 최댓값을 구합니다.\n",
      "정수 a의 값을 입력하세요.: 1\n",
      "정수 b의 값을 입력하세요.: 2\n",
      "정수 c의 값을 입력하세요.: 3\n",
      "최대값은 3입니다.\n"
     ]
    }
   ],
   "source": [
    "print('세 정수의 최댓값을 구합니다.')\n",
    "a = int(input('정수 a의 값을 입력하세요.: '))\n",
    "b = int(input('정수 b의 값을 입력하세요.: '))\n",
    "c = int(input('정수 c의 값을 입력하세요.: '))\n",
    "\n",
    "maximum = a\n",
    "if b > maximum:\n",
    "    maximum = b\n",
    "if c > maximum:\n",
    "    maximum = c\n",
    "    \n",
    "print(f'최대값은 {maximum}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 세 정수의 최댓값 구하기 알고리즘 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "max3(3, 2, 1) = 3\n",
      "max3(3, 2, 2) = 3\n",
      "max3(3, 1, 2) = 3\n",
      "max3(3, 2, 3) = 3\n",
      "max3(2, 1, 3) = 3\n",
      "max3(3, 3, 2) = 3\n",
      "max3(3, 3, 3) = 3\n",
      "max3(2, 2, 3) = 3\n",
      "max3(2, 3, 1) = 3\n",
      "max3(2, 3, 2) = 3\n",
      "max3(1, 3, 2) = 3\n",
      "max3(2, 3, 3) = 3\n",
      "max3(1, 2, 3) = 3\n"
     ]
    }
   ],
   "source": [
    "def max3(a, b, c):\n",
    "    maximum = a\n",
    "    if b > maximum:\n",
    "        maximum = b\n",
    "    if c > maximum:\n",
    "        maximum = c\n",
    "        \n",
    "    return maximum # 최댓값 반환\n",
    "\n",
    "print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')\n",
    "print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')\n",
    "print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')\n",
    "print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')\n",
    "print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')\n",
    "print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')\n",
    "print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')\n",
    "print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')\n",
    "print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')\n",
    "print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')\n",
    "print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')\n",
    "print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')\n",
    "print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 미니 실습 1)\n",
    "## 네 정수의 최댓값 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "네 정수의 최대값 구하기\n",
      "정수 a의 값을 입력하세요. :1\n",
      "정수 b의 값을 입력하세요. :4\n",
      "정수 c의 값을 입력하세요. :3\n",
      "정수 d의 값을 입력하세요. :2\n",
      "최대값은 5입니다.\n"
     ]
    }
   ],
   "source": [
    "def max4(a,b,c,d):\n",
    "    maximum=a\n",
    "    if b > maximum:\n",
    "        maximum=b\n",
    "    if c > maximum:\n",
    "        maximum=c\n",
    "    if d > maximum:\n",
    "        maximum=d\n",
    "    return maximum\n",
    "\n",
    "print('네 정수의 최대값 구하기')\n",
    "a=int(input('정수 a의 값을 입력하세요. :'))\n",
    "b=int(input('정수 b의 값을 입력하세요. :'))\n",
    "c=int(input('정수 c의 값을 입력하세요. :'))\n",
    "d=int(input('정수 d의 값을 입력하세요. :'))\n",
    "\n",
    "print(f'최대값은 {maximum}입니다.') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 조건문과 분기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 입력받은 정수의 부호(양수, 음수, 0) 출력하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요.: 0\n",
      "이 수는 0입니다.\n"
     ]
    }
   ],
   "source": [
    "n = int(input('정수를 입력하세요.: '))\n",
    "\n",
    "if n > 0:\n",
    "    print('이 수는 양수입니다.')\n",
    "elif n < 0:\n",
    "    print('이 수는 음수입니다.')\n",
    "else:\n",
    "    print('이 수는 0입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 세 정수의 중앙값 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "세 정수의 중앙값을 구합니다.\n",
      "정수 a의 값을 입력하세요.: 1\n",
      "정수 b의 값을 입력하세요.: 3\n",
      "정수 c의 값을 입력하세요.: 2\n",
      "중앙값은 2입니다.\n"
     ]
    }
   ],
   "source": [
    "def med3(a, b, c):\n",
    "    \n",
    "    if a >= b:\n",
    "        if b >= c:\n",
    "            return b\n",
    "        elif a <= c:\n",
    "            return a\n",
    "        else:\n",
    "            return c\n",
    "    elif a > c:\n",
    "        return a\n",
    "    elif b > c:\n",
    "        return c\n",
    "    else:\n",
    "        return b\n",
    "    \n",
    "print('세 정수의 중앙값을 구합니다.')\n",
    "a = int(input('정수 a의 값을 입력하세요.: '))\n",
    "b = int(input('정수 b의 값을 입력하세요.: '))\n",
    "c = int(input('정수 c의 값을 입력하세요.: '))\n",
    "\n",
    "print(f'중앙값은 {med3(a, b, c)}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 미니 실습 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 수도 요금 계산"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Unit 2. 반복하는 알고리즘"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1부터 n까지 정수의 합 구하기 (while)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1부터 n까지 정수의 합을 구합니다.\n",
      "n값을 입력하세요.: 5\n",
      "1부터 5까지 정수의 합은 15입니다.\n"
     ]
    }
   ],
   "source": [
    "print('1부터 n까지 정수의 합을 구합니다.')\n",
    "\n",
    "n = int(input('n값을 입력하세요.: '))\n",
    "\n",
    "sum = 0\n",
    "i = 1\n",
    "\n",
    "while i <= n: \n",
    "    sum += i\n",
    "    i += 1\n",
    "\n",
    "print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1부터 n까지 정수의 합 구하기 (for)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1부터 n까지 정수의 합을 구합니다.\n",
      "n값을 입력하세요.: 5\n",
      "1부터 5까지 정수의 합은 15입니다.\n"
     ]
    }
   ],
   "source": [
    "print('1부터 n까지 정수의 합을 구합니다.')\n",
    "\n",
    "n = int(input('n값을 입력하세요.: '))\n",
    "\n",
    "sum = 0\n",
    "\n",
    "for i in range(1, n+1):\n",
    "    sum += i\n",
    "\n",
    "print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### a부터 b까지 정수의 합 구하기 (for)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a부터 b까지 정수의 합을 구합니다.\n",
      "정수 a를 입력하세요.: 8\n",
      "정수 b를 입력하세요.: 3\n",
      "3부터 8까지 정수의 합은 33입니다.\n"
     ]
    }
   ],
   "source": [
    "print('a부터 b까지 정수의 합을 구합니다.')\n",
    "\n",
    "a = int(input('정수 a를 입력하세요.: '))\n",
    "b = int(input('정수 b를 입력하세요.: '))\n",
    "\n",
    "if a > b:\n",
    "    a, b = b, a\n",
    "    \n",
    "sum = 0\n",
    "\n",
    "for i in range(a, b+1):\n",
    "    sum += i\n",
    "\n",
    "print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 반복과정에서 조건 판단하기 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a부터 b까지 정수의 합을 구합니다.\n",
      "정수 a를 입력하세요.: 3\n",
      "정수 b를 입력하세요.: 4\n",
      "3 + 4 = 7\n"
     ]
    }
   ],
   "source": [
    "print('a부터 b까지 정수의 합을 구합니다.')\n",
    "\n",
    "a = int(input('정수 a를 입력하세요.: '))\n",
    "b = int(input('정수 b를 입력하세요.: '))\n",
    "\n",
    "if a > b:\n",
    "    a, b = b, a\n",
    "    \n",
    "sum = 0\n",
    "\n",
    "for i in range(a, b+1):\n",
    "    if i < b:\n",
    "        print(f'{i} + ', end='')\n",
    "    else:\n",
    "        print(f'{i} = ', end='')\n",
    "    sum +=i\n",
    "\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 미니 실습 3)\n",
    "### 반복 과정에서 조건 판단하기 (업그레이드)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 반복과정에서 조건 판단하기 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*를 출력합니다.\n",
      "몇 개를 출력할까요?: 14\n",
      "몇 개마다 줄바꿈할까요?: 5\n",
      "*****\n",
      "*****\n",
      "****\n"
     ]
    }
   ],
   "source": [
    "# * 를 n 개 출력하되 w개마다 줄바꿈하기 1 \n",
    "\n",
    "print('*를 출력합니다.')\n",
    "n = int(input('몇 개를 출력할까요?: '))\n",
    "w = int(input('몇 개마다 줄바꿈할까요?: '))\n",
    "\n",
    "for i in range(n):\n",
    "    print('*', end='')\n",
    "    if i % w == w-1:\n",
    "        print()\n",
    "\n",
    "if n%w:\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*를 출력합니다.\n",
      "몇 개를 출력할까요?: 14\n",
      "몇 개마다 줄바꿈할까요?: 5\n",
      "*****\n",
      "*****\n",
      "****\n"
     ]
    }
   ],
   "source": [
    "# * 를 n 개 출력하되 w개마다 줄바꿈하기 2 \n",
    "\n",
    "print('*를 출력합니다.')\n",
    "n = int(input('몇 개를 출력할까요?: '))\n",
    "w = int(input('몇 개마다 줄바꿈할까요?: '))\n",
    "\n",
    "for _ in range(n // w): # n//w번 반복\n",
    "    print('*' * w)      # *를 w번 출력\n",
    "   \n",
    "rest = n % w \n",
    "if rest:                # rest 값이 있으면\n",
    "    print('*' * rest)   # rest 값만큼 * 반복 출력"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 무한 루프와 break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1부터 n까지 정수의 합을 구합니다.\n",
      "n값을 입력하세요.: -6\n",
      "n값을 입력하세요.: 0\n",
      "n값을 입력하세요.: 10\n",
      "1부터 10까지 정수의 합은 55입니다.\n"
     ]
    }
   ],
   "source": [
    "# 1부터 n까지 정수의 합 구하기 (n값은 양수만 입력받음)\n",
    "\n",
    "print('1부터 n까지 정수의 합을 구합니다.')\n",
    "\n",
    "while True:\n",
    "    n = int(input('n값을 입력하세요.: '))\n",
    "    if n > 0:\n",
    "        break # n이 0보다 커질때 까지 반복\n",
    "        \n",
    "sum = 0\n",
    "i = 1\n",
    "\n",
    "for i in range(1, n+1):\n",
    "    sum += i\n",
    "    i += 1\n",
    "    \n",
    "print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### continue 와 break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정사각형의 넓이를 입력하세요.: 32\n",
      "1 x 32\n",
      "2 x 16\n",
      "4 x 8\n"
     ]
    }
   ],
   "source": [
    "# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 가능한 변의 길이 나열\n",
    "\n",
    "area = int(input('직사각형의 넓이를 입력하세요.: '))\n",
    "\n",
    "for i in range(1, area + 1):\n",
    "    if i * i > area: break       \n",
    "    if area % i: continue\n",
    "    print(f'{i} x {area // i}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 미니 실습 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 구구단 출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------------------\n",
      "  1  2  3  4  5  6  7  8  9\n",
      "  2  4  6  8 10 12 14 16 18\n",
      "  3  6  9 12 15 18 21 24 27\n",
      "  4  8 12 16 20 24 28 32 36\n",
      "  5 10 15 20 25 30 35 40 45\n",
      "  6 12 18 24 30 36 42 48 54\n",
      "  7 14 21 28 35 42 49 56 63\n",
      "  8 16 24 32 40 48 56 64 72\n",
      "  9 18 27 36 45 54 63 72 81\n",
      "---------------------------\n"
     ]
    }
   ],
   "source": [
    "print('-' * 27)\n",
    "for i in range(1, 10):\n",
    "    for j in range(1, 10):\n",
    "        print(f'{i * j:3}', end='')\n",
    "    print()\n",
    "\n",
    "print('-' * 27)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 실습 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "전기사용량을 입력하세요. :250\n",
      "전기요금은 33717원 입니다.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 실습 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+와 -를 번갈아 출력합니다.\n",
      "몇 개를 출력할까요?: 11\n",
      "+-+-+-+-+-+\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+와 -를 번갈아 출력합니다.\n",
      "몇 개를 출력할까요?: 12\n",
      "+-+-+-+-+-+-\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 실습 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 9 10 11 12 \n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 실습 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "숫자를 입력하세요.: 49\n",
      "7**2 = 49입니다.\n"
     ]
    }
   ],
   "source": [
    "# root ** pwr ( 1 < pwr < 6)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)]"
  },
  "vscode": {
   "interpreter": {
    "hash": "afb734500600fd355917ca529030176ea0ca205570884b88f2f6f7d791fd3fbe"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
