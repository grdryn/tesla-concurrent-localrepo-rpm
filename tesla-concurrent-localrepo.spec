Name:           tesla-concurrent-localrepo
Version:        0.0.3
Release:        1%{?dist}
Summary:        Tesla : Concurrent Local Repository

Group:          Development/Libraries
License:        
URL:            
Source0:        #FIXME
BuildArch: noarch

BuildRequires: mvn(com.googlecode.multithreadedtc:multithreadedtc)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.eclipse.aether:aether-test-util)
BuildRequires: mvn(io.tesla:tesla-filelock)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local

%description

    This extension for Aether contains a synchronization context that employs OS-level file locks to enable safe
    concurrent access to the local repository across processes.
  

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q #You may need to update this according to your Source0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
#FIXME
