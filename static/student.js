let allInputs = document.querySelectorAll("input")
let allLabels = document.querySelectorAll("label")
let allPs = document.querySelectorAll("p")
let allSelects = document.querySelectorAll("select")

allInputs.forEach(inputFiled => {
    inputFiled.setAttribute("class", "form-control ")
})

allLabels.forEach(label => {
    label.setAttribute("class", " col-form-label")
})

allPs.forEach(p => {
    p.setAttribute("class", "row mb-3")
})

allSelects.forEach(select => {
    select.setAttribute("class", "form-select")
})