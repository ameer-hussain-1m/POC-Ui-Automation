export let pageHeading = "//h1";
export let statusPicker="//div[@id=':r1:']";

export async function setStatus(status) {
    return (`//li[@data-value='${status}']`)
}

export let setStatusActive = "//li[@data-value='ACTIVE']";
export let setStatusInActive= "//li[@data-value='INACTIVE']";


export let productName= "//input[@name='name']";
export let productDescription= "//textarea[@name='description']";
export let stockInput = "//div[@control='[object Object]']//label[@data-shrink='false']";
export let priceInput = "//input[@aria-describedby=':r6:-helper-text']";
export let imageUploadBtn="//input[@type='file']";
export let addBtn="//button[@id=':r7:']";


