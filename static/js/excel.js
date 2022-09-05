function HtmlTOExcel(type, fun, dl) {
    let elt = document.getElementById('tableToExcel');
    let wb = XLS.utils.table_to_book(elt, { sheet: "sheet1" });
    return dl ?
        XLS.write(wb, { bookType: type, bookSST: true, type: 'base64' }) :
        XLS.writeFile(wb, fun || ('LaptopGabon-excel-document.' + (type || 'xls')));
}