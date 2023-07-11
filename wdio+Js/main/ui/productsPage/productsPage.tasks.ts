import * as locators from "./productsPage.locators";
import * as commonActions from "../../utils/browserActions.utils";
import * as assertions from "../../utils/browserAssertions.utils"


export async function checkIfProductPageIsOpen()
{
    await assertions.verifyElementIsExisting(locators.heading,"We are not on product page lol")
}

export async function addNewItem()
{
    await commonActions.click(locators.newProductBtn)
}