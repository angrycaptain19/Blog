addComment () {
    
                   fetch("/add_comment", {
                        method: "post",
                        headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            id: this.comments.length,
                            username: this.username,
                            comment: this.comment,
                            socket_id: this.socket_id
                        })
                    })
                    .then( response => response.json() )
                    .then( data => {
                        // Add the new comment to the comments state data
                        this.comments.push({
                            id: data.id,
                            username: data.username,
                            comment: data.comment,
                            sentiment: data.sentiment
                        })
    
                        // Update the sentiment score
                        this.updateSentiments();
                     })
    
                   this.username = "";
                   this.comment = "";
                });