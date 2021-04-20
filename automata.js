/*
 (nombre de la gramatica) G
S,A,B,C;a,b,z;S
S-> A
A-> a A a
A-> B
B-> b B b
B-> C
C-> z C
C-> z */

let S = { tipo: "no terminal", nombre: 'S' };
let A = { tipo: "no terminal", nombre: 'A' };
let B = { tipo: "no terminal", nombre: 'B' };
let C = { tipo: "no terminal", nombre: 'C' };

alfabeto = ['a', 'b', 'z']
simbolos_pila = [S, A, B, C, 'a', 'b', 'z', '#']

let input = '';

let size = input.length;
let state = 'i';
let stack = []
let i = 0;
while (i < size) {
    let currentChar = input.charAt(i);
    let currentChar = input.charAt(i+1);
    if (state === 'i') {
        stack.unshift('#');
        state = 'p';
    }
    else if (state === 'p') {
        stack.unshift(S);
        state = 'q';
    }
    else if (state === 'q') {
        if (typeof(stack[0]) == 'object' && stack[0].nombre === 'S') {
            stack.shift();
            stack.unshift(A);
        }
        else if (typeof(stack[0]) == 'object' && stack[0].nombre === 'A' && currentChar === 'a') {
            stack.shift();
            stack.unshift('a');
            stack.unshift(A);
            stack.unshift('a');
        }
        else if (typeof(stack[0]) == 'object' && stack[0].nombre === 'A' && currentChar === 'b') {
            stack.shift();
            stack.unshift(B);
        }
        else if (typeof(stack[0]) === 'character' && stack[0] === 'a') {
            stack.shift() // saca 'a' de la pila
            i++;
        }
        else if (typeof(stack[0]) === 'character' && stack[0] === '#') {
            stack.shift(); // sacamos '#' de la pila
            state = 'f';
        }
    }
    else if (state === 'f') {
        // aceptamos !!!!!
    }
}