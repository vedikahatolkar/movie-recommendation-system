function rateMovie(movie, rating){

fetch("/rate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
movie:movie,
rating:rating
})

})

}