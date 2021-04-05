var elems = document.getElementsByClassName('dropdown-item-confirmation');
var confirmIt = function (e) {
    if (!confirm('Confirmez-vous la suppression ?')) e.preventDefault();
};
for (var i = 0, l = elems.length; i < l; i++) {
    elems[i].addEventListener('click', confirmIt, false);
}
