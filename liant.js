const searchForm = document.getElementById('searchForm');
let parentDiv = document.getElementById("parentDiv");
const infoParag = document.getElementById('infoParag');

 //event listner for stock search
searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    infoParag.textContent = "Test 1";
    const searchFormOBJ = new FormData(searchForm);
    /*searchFormOBJ.append("userName", usernameCKB);
    searchFormOBJ.append("userPass", userPassCKB);
    searchFormOBJ.append('opcode', 'getSearchArt');*/
    getSearchData(searchFormOBJ);

    async function getSearchData(formDataSearch) {
    const editPH = "artManPH.php";
    const response = await fetch (
        editPH, 
        {
            method: 'POST',
            body: formDataSearch
        });
    const phpResponse = await response.json();

   infoParag.textContent = "Search by title results: ";
   removeChildren(parentDiv);
    
    //writeArt(phpResponse);
    }

});


//removes element children
function removeChildren(parent) {
    while (parent.hasChildNodes()) {
        parent.removeChild(parent.lastChild);
      }
}