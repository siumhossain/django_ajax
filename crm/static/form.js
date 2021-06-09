console.log('from form')


document.getElementById('submit').onclick = function() {
    console.log('submit submit');
}


const form = document.getElementById('p-form');
const resultBox = document.getElementById('resultBox');
const first_name = document.getElementById('id_first_name');
const last_name = document.getElementById('id_last_name');
const age = document.getElementById('id_age');
const agent = document.getElementById('id_agent');

const csrf = document.getElementsByName('csrfmiddlewaretoken');
const url = "";
//console.log(csrf)
//console.log(form)

form.addEventListener('submit',e=>{
    e.preventDefault() //this will prevent from page load
    const fb = new FormData();
    fb.append('csrfmiddlewaretoken',csrf[0].value)
    fb.append('first_name',first_name.value)
    fb.append('last_name',last_name.value)
    fb.append('age',age.value)
    fb.append('agent',agent.value)

    

    $.ajax({
        type:'POST',
        url:url,
        enctype: 'multipart/form-data',
        data:fb,
        success: function(response){
            resultBox.innerHTML = `
            <b>Success</b>
            `
            setTimeout(()=>{
                first_name.value = ''
                last_name.value = ''
                age.value = ''
                agent.value = ''
            },200)

            
        },
        error: function(error){
            console.log(error)
        },
        cache:false,
        contentType:false,
        processData:false,
    })
})