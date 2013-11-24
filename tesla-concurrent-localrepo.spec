%global commit 2fc6d1faf8075000f9b82676b683a18c664a359d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tesla-concurrent-localrepo
Version:        0.0.3
Release:        1%{?dist}
Summary:        Tesla : Concurrent Local Repository

License:        EPL
URL:            https://github.com/tesla/%{name}
Source0:        https://github.com/tesla/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        eclipse-1.0.txt
BuildArch:      noarch

BuildRequires: mvn(edu.umd.cs:multithreadedtc)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.eclipse.aether:aether-test-util)
BuildRequires: mvn(io.tesla:tesla-filelock)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local

%description
This extension for Aether contains a synchronization context that
employs OS-level file locks to enable safe concurrent access to the
local repository across processes.
  

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{commit}
cp %{SOURCE1} .

# Doesn't really need the parent and it's not packaged
%pom_remove_parent

# Fedora has multithreadedtc with a differend gid
%pom_remove_dep com.googlecode.multithreadedtc:multithreadedtc
%pom_add_dep edu.umd.cs:multithreadedtc

# Plugin prevents build
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc eclipse-1.0.txt

%files javadoc -f .mfiles-javadoc
%doc eclipse-1.0.txt

%changelog
* Sat Nov 23 2013 Gerard Ryan <galileo@fedoraproject.org> - 0.0.3-1
- Initial rpm
