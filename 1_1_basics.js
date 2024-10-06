// Can you write a Javascript function to add two numbers named "a" and "b" and return the result?
// function add(a, b) {
//     return a + b;
// }
// const result = add(3, 5);
// console.log(result);

// To run this JavaScript file in VSCode on a Mac, you can use the integrated terminal.
// Open the terminal in VSCode by going to View > Terminal or pressing `Ctrl + ` (backtick).
// Navigate to the directory containing your JavaScript file, if you are not already there:
// cd /Users/mahtabsyed/Documents/VSCode/Generative\ AI\ for\ Software\ Development/
// Then, run the JavaScript file using Node.js:
// node 1_Basics.js


// // Iteration 1 - Write a Javascript function to check if a number is prime
// function isPrime(num) {
//     if (num <= 1) return false;
//     if (num <= 3) return true;
//     if (num % 2 === 0 || num % 3 === 0) return false;
//     for (let i = 5; i * i <= num; i += 6) {
//         if (num % i === 0 || num % (i + 2) === 0) return false;
//     }
//     return true;
// }

// const number = 7;
// console.log(`Is ${number} a prime number? ${isPrime(number)}`);



// // Iteration 1 - In the above function can you add error conditions check
// // Error handling for isPrime function
// try {
//     const invalidNumber = -5;
//     console.log(`Is ${invalidNumber} a prime number? ${isPrime(invalidNumber)}`);
// } catch (error) {
//     console.error(`Error: ${error.message}`);
// }

// try {
//     const nonNumber = "seven";
//     console.log(`Is ${nonNumber} a prime number? ${isPrime(nonNumber)}`);
// } catch (error) {
//     console.error(`Error: ${error.message}`);
// }

// // Modify isPrime function to include error handling
// function isPrime(num) {
//     if (typeof num !== 'number') throw new Error('Input must be a number');
//     if (!Number.isInteger(num)) throw new Error('Input must be an integer');
//     if (num <= 1) return false;
//     if (num <= 3) return true;
//     if (num % 2 === 0 || num % 3 === 0) return false;
//     for (let i = 5; i * i <= num; i += 6) {
//         if (num % i === 0 || num % (i + 2) === 0) return false;
//     }
//     return true;
// }


// Iteration 3 - Can you modify above function to accept only positive integers, an dfor rest throw an error
// Modify isPrime function to accept only positive integers
function isPrime(num) {
    if (typeof num !== 'number') throw new Error('Input must be a number');
    if (!Number.isInteger(num)) throw new Error('Input must be an integer');
    if (num <= 0) throw new Error('Input must be a positive integer');
    if (num === 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
    }
    return true;
}

try {
    const invalidNumber = -5;
    console.log(`Is ${invalidNumber} a prime number? ${isPrime(invalidNumber)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}

try {
    const nonNumber = "seven";
    console.log(`Is ${nonNumber} a prime number? ${isPrime(nonNumber)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}

try {
    const validNumber = 7;
    console.log(`Is ${validNumber} a prime number? ${isPrime(validNumber)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}