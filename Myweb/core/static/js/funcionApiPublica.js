function mostrar(){
    let url='https://api.boostr.cl/holidays.json';
    fetch(url)
    .then(response => response.json())
    .then(data => mostrar(data))
    .catch(error => console.log(error))

    const mostrar=(data)=>{
        console.log(data);
        let texto=""
        for(i=0; i<data.data.length; i++)
        {
            texto+=`<tr>
                 <td>${data.data[i].date}</td>
                 <td>${data.data[i].title}</td>
                 <td>${data.data[i].type}</td>
                 <td>${data.data[i].extra}</td>
                 </tr>`
        }
        document.getElementById('datos').innerHTML=texto;
    }
}