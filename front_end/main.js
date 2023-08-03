let recipeSearch = document.querySelector('#search')
const holder = document.querySelector('.holder')

const createCard = (recipe) => {
    // CARD BUILD
    let card = document.createElement('div')
    card.className = "card"
    card.style = "width: 20rem"

    let img = document.createElement('img')
    img.src = recipe.thumbnail_url
    img.className = "card-img-top"

    let cardBody = document.createElement('div')
    cardBody.className = "card-body"

    let cardTitle = document.createElement('h3')
    cardTitle.className = "card-title"
    cardTitle.innerHTML = recipe.name

    let cardRating = document.createElement('h6')
    cardRating.className = "rating text-end"
    cardRating.innerText = `Rating: ${Math.floor(recipe.user_ratings.score * 100)}%`

    let cardText = document.createElement('p')
    cardText.className = "card-text"
    cardText.innerText = recipe.description
    
    let cardButtons = document.createElement('div')
    cardButtons.className = "card-buttons"
    
    let vidlink = document.createElement('a')
    vidlink.className = "btn btn-warning"
    vidlink.target = "_blank"
    vidlink.innerText = "Watch Video"
    vidlink.href = recipe.original_video_url    

    // MODAL BUTTON
    let fullRecipe = document.createElement('button')
    fullRecipe.type = "button"
    fullRecipe.className = "btn btn-warning"
    fullRecipe.innerText = "Show Recipe"
    fullRecipe.setAttribute("data-bs-toggle", "modal")
    fullRecipe.setAttribute("data-bs-target", `#recipeModal.${recipe.slug}`)
    

    // MODAL BUILD
    let modal = document.createElement("div")
    modal.className = "modal"
    modal.id = `recipeModal.${recipe.slug}`
    modal.setAttribute("tabindex", "-1")
    modal.setAttribute("backdrop", false)

    let modalDialog = document.createElement("div")
    modalDialog.className = "modal-dialog"
    
    let modalContent = document.createElement("div")
    modalContent.className = "modal-content"

    let modalHeader = document.createElement("div")
    modalHeader.className = "modal-header"

    let modalTitle = document.createElement("h5")
    modalTitle.className = "modal-title"
    modalTitle.innerText = recipe.name

    let modalClose = document.createElement("button")
    modalClose.className = "btn-close"
    modalClose.type = "button"
    modalClose.setAttribute("data-bs-dismiss", "modal")
    modalClose.setAttribute("aria-label", "Close")

    let modalBody = document.createElement("div")
    modalBody.className = "modal-body"

    let modalText = document.createElement("p")
    let modalBodyText = "<strong>Ingredients: </strong><br>"
        
    for (let i = 0; i < recipe.sections[0].components.length; i++) {
      let item = recipe.sections[0].components[i].raw_text;
      item = item.replace('(see recipe above)', '');
      if (item.includes('n/a')) {
        continue;
      } else {
        modalBodyText += item + "<br>";
      }
    }
        
    modalBodyText += "<br><strong>Instructions: </strong><br>";
    for (let i = 0; i < recipe.instructions.length; i++) {
      modalBodyText += `${i + 1}.) ${recipe.instructions[i].display_text}<br>`;
    }
    modalText.innerHTML = modalBodyText

    let modalFooter = document.createElement("div")
    modalFooter.className = "modal-footer"

    let modalFooterClose = document.createElement("button")
    modalFooterClose.className = "btn btn-warning"
    modalFooterClose.type = "button"
    modalFooterClose.setAttribute("data-bs-dismiss", "modal")
    modalFooterClose.innerText = "Close"

    let modalRecipeSave = document.createElement("button")
    modalRecipeSave.className = "btn btn-warning"
    modalRecipeSave.type = "button"
    modalRecipeSave.setAttribute("data-bs-dismiss", "modal")
    modalRecipeSave.innerText = "Save"   
    // END MODAL BUILD

    
    cardButtons.appendChild(vidlink)
    cardButtons.appendChild(fullRecipe)
    cardBody.appendChild(cardTitle)
    cardBody.appendChild(cardRating)
    cardBody.appendChild(cardText)
    cardBody.appendChild(cardButtons)
    card.appendChild(img)
    card.appendChild(cardBody)
    holder.appendChild(card)

    modalHeader.appendChild(modalTitle)
    modalHeader.appendChild(modalClose)
    modalBody.appendChild(modalText)
    modalFooter.appendChild(modalFooterClose)
    modalFooter.appendChild(modalRecipeSave)
    modalContent.appendChild(modalHeader)
    modalContent.appendChild(modalBody)
    modalContent.appendChild(modalFooter)
    modalDialog.appendChild(modalContent)
    modal.appendChild(modalDialog)

    holder.appendChild(modal)
        
}


const options = {
    method: 'GET',
    url: 'https://tasty.p.rapidapi.com/recipes/list',
    params: {
      from: '0',
      size: '200',
      tags: '',
      q: recipeSearch.value
    },
    headers: {
      'X-RapidAPI-Key': "",
      'X-RapidAPI-Host': 'tasty.p.rapidapi.com'
    }
};

//  API CALL WITH INPUT UPDATE
const getRecipe = async() => {
    while (holder.firstChild) {
        holder.removeChild(holder.firstChild)
    }
    
    let apikey = await import("./key.js")
    let MYKEY = apikey.MYAPIKEY

    options.headers["X-RapidAPI-Key"] = MYKEY

    options.params.q = recipeSearch.value
    try {
        console.log(recipeSearch.value)
        const response = await axios.request(options)
        console.log(response.data)
        for (i=0; i<response.data.results.length; i++) {
            createCard(response.data.results[i])
        }
    } catch {
        console.error(error)
    }
}

// JSON CALL *** DON"T FORGET TO RUN SERVER *** 
// async function getRecipe() {
//     while (holder.firstChild) {
//         holder.removeChild(holder.firstChild)
//     }

//     const url = 'http://localhost:3000/results'
//     let data = await fetch(url)
//     let recipes = await data.json()

//     for (i=0; i<recipes.length; i++) {
//         createCard(recipes[i])

//     }
   
// }

