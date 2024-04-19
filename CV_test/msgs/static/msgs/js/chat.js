function settaker(anElement) {
    var input = document.getElementById('id_take');
    let params = new URLSearchParams(document.location.search);
    params.set('im', anElement.innerText);
    window.history.replaceState(null, '', '?' + params);
    $("#soob").load(location.href+" #soob>*","");
    input.value = anElement.innerText;
    anElement.style = "background: #dd1133"
}


