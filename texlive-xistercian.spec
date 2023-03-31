Name:		texlive-xistercian
Version:	61366
Release:	2
Summary:	Cistercian numerals in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xistercian
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xistercian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xistercian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xistercian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
xistercian allows you to use Cistercian numerals in LaTeX. The
glyphs are created using PGF and to a certain degree
configurable. You can use Cistercian numerals as page numbers
using \pagenumbering{cistercian}. The two main macros are:
\cistercian{<counter>} formats the LaTeX2e counter as a
Cistercian numeral \cisterciannum{<integer>} formats the
integer (given as a string) as a Cistercian numeral

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xistercian
%{_texmfdistdir}/tex/latex/xistercian
%doc %{_texmfdistdir}/doc/latex/xistercian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
