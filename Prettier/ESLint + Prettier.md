ESlint 与 Prettier 可能会冲突，需要安包配置：

## 1. 安装配置：

我们需要使用 `eslint-config-prettier` 来关掉 (disable) 所有和 Prettier 冲突的 ESLint 的配置

```bash
npm install eslint-config-prettier -D
```
在 `.eslintrc` 里面将 prettier 设为最后一个 extends

```javascript
// .eslintrc    
{      
    "extends": ["prettier"] // prettier 一定要是最后一个，才能确保覆盖    
}
```

## 2. 安装插件（可选）：

将 prettier 的 rules 以插件的形式加入到 ESLint 里面，其实是因为我们期望报错的来源依旧是 ESLint 

使用这个相当于把 Prettier 推荐的格式问题的配置以 ESLint rules 的方式写入，这样相当于可以统一代码问题的来源

```bash
npm install eslint-plugin-prettier -D
```

```javascript
// .eslintrc    
{      
    "plugins": ["prettier"],      
    "rules": {        
        "prettier/prettier": "error"      
    }    
}
```

## 3. 上面两个整合：

```bash
npm install eslint-config-prettier eslint-plugin-prettier -D
```

将上面两个步骤和在一起就是下面的配置，官方的推荐配置：

```javascript
// .eslintrc
{
  "extends": ["plugin:prettier/recommended"]
}
```