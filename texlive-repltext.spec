# revision 33442
# category Package
# catalog-ctan /macros/latex/contrib/repltext
# catalog-date 2014-04-14 00:47:26 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-repltext
Version:	1.0
Release:	3
Summary:	Control how text gets copied from a PDF file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/repltext
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The repltext package exposes to LaTeX a relatively obscure PDF
feature: replacement text. When replacement text is specified
for a piece of text, it is the replacement text, not the
typeset text that is copied and pasted.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/repltext/repltext.sty
%doc %{_texmfdistdir}/doc/latex/repltext/README
%doc %{_texmfdistdir}/doc/latex/repltext/repltext.pdf
#- source
%doc %{_texmfdistdir}/source/latex/repltext/repltext.dtx
%doc %{_texmfdistdir}/source/latex/repltext/repltext.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
