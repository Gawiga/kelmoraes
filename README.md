# 🌿 Kelmoraes - Psicóloga Clínica

[![Netlify Status](https://api.netlify.com/api/v1/badges/8194162e-0be2-4687-affd-5faf1c8b7f7f/deploy-status)](https://app.netlify.com/sites/kelmoraes/deploys)
[![CI](https://github.com/gawiga/kelmoraes/actions/workflows/ci.yml/badge.svg)](https://github.com/gawiga/kelmoraes/actions/workflows/ci.yml)
[![CodeQL](https://github.com/gawiga/kelmoraes/actions/workflows/codeql.yml/badge.svg)](https://github.com/gawiga/kelmoraes/actions/workflows/codeql.yml)

Site institucional da psicóloga clínica Raquel Moraes, com atendimento online e presencial em Jundiaí/SP. Design renascentista, one-page, mobile-first.

---

## 🎨 Design

Layout inspirado na estética renascentista com:
- Tipografia serifada elegante (Cormorant Garamond + Playfair Display)
- Paleta quente: cream, burgundy, gold
- Ornamentos sutis e divisores decorativos
- Animações suaves e refinadas

---

## 🛠️ Stacks & Tecnologias

### Core
| Tecnologia | Versão | Função |
|------------|--------|--------|
| [Jekyll](https://jekyllrb.com/) | 4.4.1 | Gerador de site estático |
| [Ruby](https://www.ruby-lang.org/) | 3.3.5 | Linguagem de programação |
| [Sass/SCSS](https://sass-lang.com/) | Embedded 1.94 | Pré-processador CSS |
| [Liquid](https://shopify.github.io/liquid/) | 4.0 | Template engine |

### Plugins Jekyll
| Plugin | Função |
|--------|--------|
| `jekyll-seo-tag` | SEO e meta tags automáticas |
| `jekyll-feed` | Geração de feed RSS |
| `jekyll-sitemap` | Sitemap.xml automático |

### Frontend
| Tecnologia | Função |
|------------|--------|
| Google Fonts | Cormorant Garamond, Playfair Display, Lato |
| Schema.org | JSON-LD para SEO local (Psychologist) |
| Open Graph | Meta tags para redes sociais |
| CSS Grid/Flexbox | Layout responsivo mobile-first |

### Hospedagem & Deploy
| Serviço | Função |
|---------|--------|
| [Netlify](https://www.netlify.com/) | Hospedagem e deploy automático |
| GitHub | Repositório e versionamento |

### CI/CD & Qualidade
| Ferramenta | Função |
|------------|--------|
| GitHub Actions (CI) | Build e testes automatizados |
| GitHub Actions (CodeQL) | Análise de segurança estática |
| HTMLProofer | Validação de HTML e links quebrados |
| pytest | Testes de integração Python |

### Segurança
| Recurso | Implementação |
|---------|---------------|
| Content Security Policy | Meta tags + netlify.toml |
| X-Content-Type-Options | nosniff |
| X-Frame-Options | DENY |
| Referrer-Policy | strict-origin-when-cross-origin |
| Google Analytics | gtag.js com anonymize_ip (LGPD) |
| Links externos | rel="noopener noreferrer" |

---

## 📁 Estrutura do Projeto

```
kelmoraes/
├── _config.yml           # Configurações do site
├── _config-dev.yml       # Configurações de desenvolvimento
├── _includes/            # Partial templates
│   ├── header.html       # Header/hero section
│   ├── footer.html       # Footer com navegação
│   ├── instagram.html    # Embed do Instagram
│   ├── analytics-google.html
│   └── style.scss        # Sass entry point
├── _layouts/             # Layout templates
│   ├── default.html      # Layout base
│   └── home.html         # Layout da home
├── _sass/                # Sass partials
│   ├── base/             # Variáveis, tipografia, resets
│   ├── components/       # Header, footer, nav, social
│   └── pages/            # Estilos específicos de páginas
├── assets/               # Imagens e assets
├── tests/                # Testes de integração
│   └── integration/
│       └── test_site.py  # pytest tests
├── .github/workflows/    # GitHub Actions
│   ├── ci.yml            # CI pipeline
│   └── codeql.yml        # CodeQL security analysis
├── index.html            # Página principal (one-page)
├── cuidados.html         # Página de cuidados pré/pós tattoo
├── privacidade.md        # Política de privacidade (LGPD)
├── netlify.toml          # Configurações Netlify + security headers
└── Gemfile               # Ruby dependencies
```

---

## 🚀 Como Rodar

### Pré-requisitos
- **Ruby** 3.0+ (atualmente 3.3.5)
- **Bundler**: `gem install bundler`
- **Python** 3.8+ (para testes)

### Instalação

```bash
# Instalar dependências Ruby
bundle install

# Instalar dependências Python (para testes)
pip install pytest beautifulsoup4 lxml
```

### Desenvolvimento

```bash
# Servidor local com auto-reload
bundle exec jekyll serve --config _config.yml,_config-dev.yml

# Site disponível em: http://localhost:4000
```

### Build Produção

```bash
# Gerar site estático
bundle exec jekyll build

# Output em: _site/
```

### Testes

```bash
# Build + HTMLProofer (links quebrados)
bundle exec rake test

# Testes de integração pytest
pytest tests/integration/test_site.py -v
```

---

## 📝 Comandos Úteis

```bash
# Atualizar dependências
bundle update

# Build com trace de erros
bundle exec jekyll build --trace

# Servidor com livereload
bundle exec jekyll serve --livereload

# Testes verbose
pytest tests/integration/test_site.py -v --tb=short
```

---

## 🔒 Segurança

O projeto implementa:
- ✅ Content Security Policy (CSP)
- ✅ Google Analytics com anonymize_ip (LGPD compliant)
- ✅ Links externos com `rel="noopener noreferrer"`
- ✅ CodeQL Analysis automatizada
- ✅ Headers de segurança no netlify.toml
- ✅ Página de política de privacidade

---

## 📄 Licença

[MIT](http://kopplin.mit-license.org/) License © Sérgio Kopplin

[Fork deste template](https://github.com/sergiokopplin/indigo)

---

> Desenvolvido por [Gawiga](http://www.gawiga.com/)
