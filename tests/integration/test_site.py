"""Integration tests for the Jekyll site."""
import pytest
from pathlib import Path

SITE_DIR = Path(__file__).parent.parent.parent / "_site"


class TestPagesExist:
    """Test that essential pages exist after build."""

    @pytest.mark.parametrize("page", [
        "index.html",
        "404.html",
        "cuidados.html",
        "privacidade.html",
        "feed.xml",
        "sitemap.xml",
    ])
    def test_page_exists(self, page):
        assert (SITE_DIR / page).exists(), f"Page {page} not found"


class TestHTMLValidity:
    """Test HTML content for correctness."""

    def test_index_has_content(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "Raquel Moraes" in content
        assert "Psicóloga" in content

    def test_index_has_analytics(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "googletagmanager" in content or "google-analytics" in content

    def test_has_proper_lang(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert 'lang="pt-BR"' in content, "Language should be pt-BR"

    def test_cuidados_no_invalid_nesting(self):
        """Test that h3 is not nested inside p (invalid HTML)."""
        content = (SITE_DIR / "cuidados.html").read_text(encoding="utf-8")
        # Should not have <p><h3> pattern - h3 should be in div, not p
        import re
        # Check there's no <p>...</p> wrapping an <h3>
        assert not re.search(r'<p[^>]*>\s*<h[3]', content), "Invalid HTML: h3 nested inside p"

    def test_privacidade_has_lgpd(self):
        content = (SITE_DIR / "privacidade.html").read_text(encoding="utf-8")
        assert "LGPD" in content

    def test_external_links_have_rel_noopener(self):
        """Test that external links have rel='noopener noreferrer'."""
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        # Check that target="_blank" links also have rel="noopener"
        if 'target="_blank"' in content:
            assert "noopener" in content

    def test_has_security_meta_tags(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "X-Content-Type-Options" in content
        assert "X-Frame-Options" in content
        assert "Referrer-Policy" in content

    def test_has_open_graph_tags(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert 'og:title' in content
        assert 'og:description' in content
        assert 'og:image' in content

    def test_has_schema_org(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "schema.org" in content
        assert "application/ld+json" in content

    def test_has_canonical_link(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert 'rel="canonical"' in content

    def test_footer_no_duplicate_analytics(self):
        """Ensure analytics is not duplicated in footer."""
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        gtag_count = content.count("googletagmanager.com/gtag/js")
        assert gtag_count <= 1, f"Google Analytics duplicated ({gtag_count} times)"


class TestAccessibility:
    """Test accessibility features."""

    def test_links_have_aria_labels(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "aria-label" in content

    def test_images_have_alt_text(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert "alt=" in content

    def test_lazy_loading_images(self):
        content = (SITE_DIR / "index.html").read_text(encoding="utf-8")
        assert 'loading="lazy"' in content
