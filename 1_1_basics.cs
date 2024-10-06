// Write a C# method to add two numbers
using System;

namespace Basics
{
    class Program
    {
        static void Main(string[] args)
        {
            int number1 = 5;
            int number2 = 10;
            int result = AddNumbers(number1, number2);
            Console.WriteLine($"The sum of {number1} and {number2} is {result}");
        }

        static int AddNumbers(int a, int b)
        {
            return a + b;
        }
    }
}