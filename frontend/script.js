const apiUrl = "http://localhost:8000";

// Get all furniture items and display them in a table
function getAllFurniture() {
  fetch(`${apiUrl}/furniture/getFurniture`)
    .then((response) => response.json())
    .then((furnitureList) => {
      if (furnitureList.data.length !== 0) {
        const table = document.getElementById("furniture-table");
        table.innerHTML = "";
        furnitureList.data.forEach((furniture) => {
          const row = table.insertRow();
          if (furniture.comment === null) {
            row.innerHTML = `<td>${furniture.name}</td>
                              <td>${furniture.description}</td>
                              <td>$${furniture.price}</td>
                              <td>No Comments are added</td>
                              <td><button onclick="addComment(${furniture.id})">Add Comment</button></td>`;
          } else {
            row.innerHTML = `<td>${furniture.name}</td>
                              <td>${furniture.description}</td>
                              <td>$${furniture.price}</td>
                              <td>${furniture.comment}</td>
                              <td><button onclick="addComment(${furniture.id})">Add Comment</button></td>`;
          }
        });
      }
    });
}

// Add a new furniture item
function addFurniture() {
  const nameInput = document.getElementById("name-input");
  const descriptionInput = document.getElementById("description-input");
  const priceInput = document.getElementById("price-input");

  if (priceInput.value === "") {
    alert("Price can be empty");
  } else if (priceInput.value == 0) {
    alert("Price can't be 0");
  } else {
    const newFurniture = {
      name: nameInput.value,
      description: descriptionInput.value,
      price: priceInput.value,
    };
    fetch(`${apiUrl}/furniture/addFurniture`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newFurniture),
    })
      .then((response) => response.json())
      .then((furniture) => {
        getAllFurniture();
        nameInput.value = "";
        descriptionInput.value = "";
        priceInput.value = "";
      });
  }
}

// Add a comment to a furniture item
function addComment(furniture_id) {
  const commentInput = prompt("Enter your comment:");
  fetch(`${apiUrl}/comment/${furniture_id}/addComment`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ comment: commentInput }),
  })
    .then((response) => response.json())
    .then((furniture) => getAllFurniture());
}

// Search furniture
function searchFurniture() {
  const search_input = document.getElementById("search-input");
  const input = {
    pattern: search_input.value,
  };
  if (search_input.value === "") {
    alert("Please enter some comment");
  } else {
    fetch(`${apiUrl}/comment/getCommentFurniture`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(input),
    })
      .then((response) => response.json())
      .then((furnitureList) => {
        const table = document.getElementById("furniture-table");
        if (furnitureList.data.length !== 0) {
          table.innerHTML = "";
          furnitureList.data.forEach((furniture) => {
            const row = table.insertRow();
            row.innerHTML = `<td>${furniture.name}</td>
                          <td>${furniture.description}</td>
                          <td>$${furniture.price}</td>
                          <td>${furniture.comment}</td>
                          <td><button onclick="addComment(${furniture.id})">Add Comment</button></td>`;
          });
        } else {
          table.innerHTML = `<td>NO FURNITURE WAS FOUND FOR COMMENT : ${input.pattern}</td>`;
        }
      });
  }
}

getAllFurniture();
