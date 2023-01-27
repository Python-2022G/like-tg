# like-bot

## steps:
### 1 - create repository

### 2 - clone repository
```bash 
git clone URL
```

### 3 - change directory
```bash
cd repo
```

### 4 - create venv
```bash
python -m venv venv
```

### 5 - activate
```bash
source venv/Scripts/activate
```

### 6 - .gitingore and requirements.txt
```bash
touch .gitignore requirements.txt
```

### 7 - packages in requirements.txt

### 8 - install
```bash
pip install -r requirements.txt
```

### 9 - env TOKEN
```bash
export TOKEN={token}
```

### 10 - print TOKEN env
```bash
echo $TOKEN
```

### 11 - start code


# json file
```json
{
    "123456":{
        "likes": 0,
        "dislikes": 0,
    },
    "123455":{
        "likes": 1,
        "dislikes": 0,
    },
    "1345356":{
        "likes": 0,
        "dislikes": 1,
    }
}
```


### data base CRUD
- C (create) 
- R (read) 
- U (update) 
- D (delete) 
