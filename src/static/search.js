function searchCharacters() {
    let input, filter, table, tr, td, i, txtValue;

    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("characterTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1]; //Get the td with the name in it
        if (td) {
            txtValue = td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}