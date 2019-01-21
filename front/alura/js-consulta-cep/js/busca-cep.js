var botaoBuscar = document.querySelector('#btn-buscar');

botaoBuscar.addEventListener('click', function(event){
    event.preventDefault();
    buscaCEP();
});

function buscaCEP(){
    var inputCEP = document.querySelector('input[name=cep]');
    var url = 'http://viacep.com.br/ws/' + inputCEP.value + '/json';
    var xhr = new XMLHttpRequest();
    
    xhr.open('GET', url);
    xhr.addEventListener('load', function(){
        if(xhr.status == 200){
            var resposta = xhr.responseText;
            var json = JSON.parse(resposta);
            preencheCampos(json);
        }
        else{
            console.log(xhr.status);
            console.log(xhr.responseText);
        }
    });
    xhr.send();
}

function preencheCampos(json){
    document.querySelector('input[name=endereco]').value = json.logradouro;
    document.querySelector('input[name=bairro]').value = json.bairro;
    document.querySelector('input[name=complemento]').value = json.complemento;
    document.querySelector('input[name=cidade]').value = json.localidade;
    document.querySelector('input[name=estado]').value = json.uf;
}