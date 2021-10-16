// select db 'localStorage'. request item 'on_load_counter'
var counts = localStorage.getItem('on_load_counter');

if (counts === null) {
counts = 0;
}

counts++;


// select db 'localStorage'. Set item 'on_load_counter' to variable 'counts'
localStorage.setItem("on_load_counter", counts);


document.getElementById('CounterVisitor').innerHTML = counts;



// var n = localStorage.getItem('on_load_counter');

// if (n === null) {
//     n = 0;
// }

// if (n === NaN) {
//     n = 0;
// }

// n++;

// localStorage.setItem("on_load_counter", n);

// document.getElementById('CounterVisitor').innerHTML = n;