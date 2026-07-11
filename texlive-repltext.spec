%global tl_name repltext
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Control how text gets copied from a PDF file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/repltext
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/repltext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The repltext package exposes to LaTeX a relatively obscure PDF feature:
replacement text. When replacement text is specified for a piece of
text, it is the replacement text, not the typeset text that is copied
and pasted.

