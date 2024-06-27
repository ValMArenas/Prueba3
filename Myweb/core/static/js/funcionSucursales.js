function mostrarSucursales(){
    let url='http://localhost:3000/sucursales';
    fetch(url)
    .then(response => response.json())
    .then(data => mostrarSucursales(data))
    .catch(error => console.log(error))

    const mostrarSucursales=(data)=>{
        console.log(data);
        let texto=""
        for(i=0; i<data.length; i++)
        {
            texto+=`<tr>
                 <td>${data[i].calle}</td>
                 <td>${data[i].comuna}</td>
                 <td>${data[i].tipo}</td>
                 </tr>`
        }
        document.getElementById('sucursales').innerHTML=texto;
    }
}

function buscarComuna(){
    let url='http://localhost:3000/sucursales';
    fetch (url)
    .then(response=>response.json())
    .then(data => buscarComuna(data))
    .catch(error => console.log(error))

    const buscarComuna=(data)=>{
        console.log(data);
        let texto="";
        let comuna=document.getElementById('comuna').value;

        if (document.getElementById('comuna').selectedIndex==0){
            mostrarSucursales();

        }else{
            for(i=0; i<data.length; i++)
                {
                    if (comuna==data[i].comuna){
                        texto+=`<tr>
                         <td>${data[i].calle}</td>
                         <td>${data[i].comuna}</td>
                         <td>${data[i].tipo}</td>
                         </tr>`
                    }
                }
                document.getElementById('sucursales').innerHTML=texto;
        }   
    }
}