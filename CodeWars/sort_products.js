function sortProducts (matrix) {
    const tech = [];
    const food = [];
    
    for (let i = 0; i < matrix.length; i++) {
      const arr = matrix[i];
  
      for (let j = 0; j < arr.length; j++) {
        const product = arr[j];
        
        if ( product.category === 'tech') {
          tech.push(product);
  //         tech.unshift(product);
        }
        else if (product.category === 'food') {
          food.push(product);
  //         food.unshift(product);
        }
      };
    };  
    
    return {
      tech: tech,
      food: food,
    }
  }