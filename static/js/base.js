function addIngredientField() {
    const container = document.getElementById('ingredients-container');
    const input = document.createElement('input');
    input.type = 'text';
    input.name = 'ingredients';
    input.required = true;
    input.placeholder = 'Input Ingredient here...';
    container.append(input);
    container.append(document.createElement('br'));
  
}

function addInstructionField() {
    const container = document.getElementById('instructions-container');
    const textarea = document.createElement('textarea');
    textarea.name = 'instruction';
    textarea.required = true;
    textarea.placeholder = 'Input Instruction here...';
    container.append(textarea);
    container.append(document.createElement('br'));
}
