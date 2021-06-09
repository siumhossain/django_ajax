
console.log('hello2');
//finding location of current page
//const url = "http://127.0.0.1:8000/";

const url = window.location.href;
console.log(url);
//console.log(url);

const searchForm = document.getElementById('search-form');

//console.log(searchForm)

const searchInput = document.getElementById('search-input');

const resultBox = document.getElementById('result-box');
//console.log(resultBox)
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

//console.log(csrf)

const sendSearchData = (people) =>{
    $.ajax({
        type: "POST",
        url: 'search/',
        data:{
            "csrfmiddlewaretoken":csrf,
            "people":people,
        },
        success: (res) =>{
            console.log(res.data);
            const data = res.data;
            if(Array.isArray(data)){
                console.log('get array')
                resultBox.innerHTML=''
                data.forEach(people =>{
                    resultBox.innerHTML += `
                        <div>
                            ${people.first_name}
                        </div>
                    `
                })

            }
            else{
                if(searchInput.value.length>0){
                    resultBox.innerHTML = `<br><b>${data}</b><br>`
                }//else{
                    //resultBox.classList.add('not visible')
            //}
            }
        },
        error: (err) => {
            console.log(err)
        }
    })


}
//input value in console 

searchInput.addEventListener('keyup', e=>{
    //console.log(e.target.value)
    sendSearchData(e.target.value)
} )


