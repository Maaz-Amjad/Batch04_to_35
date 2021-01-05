{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy_Assignment_2::"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert a 1D array to a 2D array with 2 rows?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired output::"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4],\n",
    "        [5, 6, 7, 8, 9]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1 = np.array([1,2,3,4,5,6,7,8,9,10])\n",
    "arr1.reshape(2,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  How to stack two arrays vertically?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4],\n",
    "        [5, 6, 7, 8, 9],\n",
    "       [1, 1, 1, 1, 1],\n",
    "       [1, 1, 1, 1, 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2],\n",
       "       [ 3,  4],\n",
       "       [ 5,  6],\n",
       "       [ 7,  8],\n",
       "       [ 9, 10],\n",
       "       [11, 12],\n",
       "       [13, 14],\n",
       "       [15, 16],\n",
       "       [17, 18],\n",
       "       [19, 20]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2 = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(5,2)\n",
    "arr3 = np.array([11,12,13,14,15,16,17,18,19,20]).reshape(5,2)\n",
    "np.vstack((arr2,arr3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to stack two arrays horizontally?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],\n",
    "       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2, 11, 12],\n",
       "       [ 3,  4, 13, 14],\n",
       "       [ 5,  6, 15, 16],\n",
       "       [ 7,  8, 17, 18],\n",
       "       [ 9, 10, 19, 20]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr4 = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(5,2)\n",
    "arr5 = np.array([11,12,13,14,15,16,17,18,19,20]).reshape(5,2)\n",
    "np.hstack((arr4,arr5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to convert an array of arrays into a flat 1d array?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 0  1]\n",
      "  [ 2  3]\n",
      "  [ 4  5]\n",
      "  [ 6  7]\n",
      "  [ 8  9]]\n",
      "\n",
      " [[10 11]\n",
      "  [12 13]\n",
      "  [14 15]\n",
      "  [16 17]\n",
      "  [18 19]]\n",
      "\n",
      " [[20 21]\n",
      "  [22 23]\n",
      "  [24 25]\n",
      "  [26 27]\n",
      "  [28 29]]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6 = np.arange(30).reshape(3,5,2)\n",
    "print(arr6)\n",
    "np.reshape(arr6,(30))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to Convert higher dimension into one dimension?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])"
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
      "3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6 = np.arange(30).reshape(3,2,5)\n",
    "print(arr6.ndim)\n",
    "np.reshape(arr6,(30)).ndim"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert one dimension to higher dimension?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[ 0, 1, 2],\n",
    "[ 3, 4, 5],\n",
    "[ 6, 7, 8],\n",
    "[ 9, 10, 11],\n",
    "[12, 13, 14]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr7 = np.arange(30)\n",
    "print(arr7.ndim)\n",
    "np.reshape(arr7,(5,2,3)).ndim"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create 5x5 an array and find the square of an array?"
   ]
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
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [10 11 12 13 14]\n",
      " [15 16 17 18 19]\n",
      " [20 21 22 23 24]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[  0,   1,   4,   9,  16],\n",
       "       [ 25,  36,  49,  64,  81],\n",
       "       [100, 121, 144, 169, 196],\n",
       "       [225, 256, 289, 324, 361],\n",
       "       [400, 441, 484, 529, 576]], dtype=int32)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr8 = np.arange(25).reshape(5,5)\n",
    "print(arr8)\n",
    "np.square(arr8)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:8"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create 5x6 an array and find the mean?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The mean of he array 8.65544144839919'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr9 = np.arange(30).reshape(5,6)\n",
    "f\"The mean of he array {arr9.std()}\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the standard deviation of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The standard daviation of the above array 8.65544144839919'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f\"The standard daviation of the above array {arr9.std()}\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the median of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14.5"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.median(arr9)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the transpose of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  6, 12, 18, 24],\n",
       "       [ 1,  7, 13, 19, 25],\n",
       "       [ 2,  8, 14, 20, 26],\n",
       "       [ 3,  9, 15, 21, 27],\n",
       "       [ 4, 10, 16, 22, 28],\n",
       "       [ 5, 11, 17, 23, 29]])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr9.transpose()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:12"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a 4x4 an array and find the sum of diagonal elements?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  6  7  8]\n",
      " [ 9 10 11 12]\n",
      " [13 14 15 16]\n",
      " [17 18 19 20]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr10 = np.arange(5,21).reshape(4,4)\n",
    "print(arr10)\n",
    "np.trace(arr10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:13"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the determinant of the previous array in Q12?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.3755762034791435e-29"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linalg.det(arr10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:14"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the 5th and 95th percentile of an array?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5th percentile of arr :  2.45\n",
      "95th percentile of arr :  46.55\n"
     ]
    }
   ],
   "source": [
    "arr11 = np.arange(50)\n",
    "print(\"5th percentile of arr : \", \n",
    "       np.percentile(arr11, 5))\n",
    "print(\"95th percentile of arr : \", \n",
    "       np.percentile(arr11, 95))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:15"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to find if a given array has any null values?"
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
      "\n",
      "Is NaN: \n",
      " [[False False False False False]\n",
      " [False False False False False]\n",
      " [False False False False False]\n",
      " [False False False False False]\n",
      " [False False False False False]]\n",
      "\n",
      "Is NaN: \n",
      " [[False False False False]\n",
      " [ True False False False]]\n"
     ]
    }
   ],
   "source": [
    "arr12 = np.arange(25).reshape(5, 5)             \n",
    "print(\"\\nIs NaN: \\n\", np.isnan(arr12)) \n",
    "arr13 = [[1,2,3,4],  \n",
    "     [np.nan,2,2,2]] \n",
    "print(\"\\nIs NaN: \\n\", np.isnan(arr13)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
